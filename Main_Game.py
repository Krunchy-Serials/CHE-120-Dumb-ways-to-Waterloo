#!/usr/bin/env python3
"""
Main launcher for "Dumb Ways to Waterloo" minigames.

This file implements a small CLI minigame launcher used for a CHE-120
class. It discovers minigames in the same directory, loads them
dynamically, and presents a short menu for students to play:

 - Start a randomized survival mode (play until you lose all lives)
 - Play a single minigame by selecting it from the list
 - Change the difficulty (affects time limits passed to minigames)
 - Toggle "Cruel Mode" (enables time-limit reduction as you score)
 - View credits and quit

This file focuses on simplicity and readability for beginners
while demonstrating basic Python modules, dynamic imports, and
CLI interaction. It also includes lightweight gameplay features:

- Emoji feedback for success/failure and lives (e.g., ✅, ❌, ❤️, 💔).
- Persistent high score tracking (stored in `highscore.txt` next to this file).
- Cruel Mode: in survival mode, time limits decrease a small amount
    for every few successful minigames, making the game harder over time.
"""
import importlib.util
import os
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
# Directory of this script; used to find minigame files nearby.

 # List of minigame module filenames to load. To add a minigame, add its filename here.
MINIGAME_MODULE_FILES = [
    "Safety_Inspection_Minigame.py",
    "do_your_homework.py",
    "find_exam_desk.py",
    "dana_porter_elevator.py",
    "Sarah V1.py",
    "Madi's_Contribution.py",
]

# High score storage (stored in the project directory)
HIGH_SCORE_FILE = ROOT / "highscore.txt"


def load_module(path: Path):
    """
    Dynamically load a Python module from a file path.
    """
    spec = importlib.util.spec_from_file_location(path.stem, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def get_minigames(mod):
    """
    Find all minigame functions in a module.
    Prefers a MINIGAMES list, otherwise looks for common function names.
    Returns a list of (function, label) pairs.
    """
    res = []
    # If module exports MINIGAMES list, use it directly
    if hasattr(mod, "MINIGAMES"):
        for fn in getattr(mod, "MINIGAMES"):
            res.append((fn, f"{mod.__name__}.{fn.__name__}"))
        return res

    # otherwise look for `run` / common function names
    candidates = ["run", "safety_inspection_minigame", "do_your_homework", "find_exam_desk", "escape_dana_porter_elevator"]
    for name in candidates:
        if hasattr(mod, name):
            fn = getattr(mod, name)
            if callable(fn):
                res.append((fn, f"{mod.__name__}.{name}"))
    return res


def discover_all():
    minigame_functions = []  # List to hold all discovered minigame functions
    for module_filename in MINIGAME_MODULE_FILES:
        path = ROOT / module_filename
        if not path.exists():
            continue
        mod = load_module(path)
        found = get_minigames(mod)
        minigame_functions.extend(found)
    return minigame_functions


def call_minigame(fn, time_limit=None):
    """
    Call a minigame function, passing the time limit if possible.
    Returns True if the minigame is won, False otherwise.
    """
    try:
        return bool(fn(time_limit=time_limit))
    except TypeError:
        # If function doesn't accept time_limit, call without
        try:
            return bool(fn())
        except Exception as error:
            print("Minigame raised error:", error)
            return False
    except Exception as error:
        print("Minigame raised error:", error)
        return False


def hearts_display(lives: int) -> str:
    """Return a short string of heart emojis based on remaining lives.
    If lives is 0 or below, returns a broken-heart emoji.
    """
    if lives <= 0:
        return "💔"
    return " ".join(["❤️"] * lives)


def read_high_score() -> int:
    """Return stored high score or 0 if none found."""
    try:
        if HIGH_SCORE_FILE.exists():
            text = HIGH_SCORE_FILE.read_text().strip()
            if text.isdigit():
                return int(text)
    except Exception:
        pass
    return 0


def save_high_score(score: int):
    """Write a new high score to disk."""
    try:
        HIGH_SCORE_FILE.write_text(str(score))
    except Exception:
        # If write fails, ignore; high score is optional
        pass


def clear():
    """
    Clear the terminal screen for better readability.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def print_menu(menu):
    """
    Print a numbered menu of minigame options.
    """
    print("Choose a minigame to play:\n")
    for i, minigame_label in enumerate(menu, 1):
        print(f" [{i}] {minigame_label}")
    print()


def get_choice(menu_len):
    """
    Get a valid menu choice from the user.
    Returns the selected number, or None if invalid.
    """
    user_input = input("Your choice: ").strip()
    if not user_input.isdigit():
        return None
    choice_num = int(user_input)
    if choice_num < 1 or choice_num > menu_len:
        return None
    return choice_num


def play_single_game(fn, label, time_limit=None):
    clear()
    tl = f" ({time_limit}s)" if time_limit is not None else ""
    print(f"Playing: {label}{tl}\n")
    success = call_minigame(fn, time_limit=time_limit)
    # Tick or cross emoji depending on outcome
    if success:
        print("Result: ✅ Success")
    else:
        print("Result: ❌ Failed")
    input("Press ENTER to continue...")
    return success


def play_survival(minigames, lives=3, time_limit=None, cruel_mode=False):
    """
    Play all minigames in random order until lives run out.
    Each win increases score, each loss decreases lives.
    """
    remaining_minigame_indices = list(range(len(minigames)))
    random.shuffle(remaining_minigame_indices)
    score = 0
    current_time_limit = time_limit
    # Track when to make things cruel: after this many successes reduce time
    cruel_decrement_every = 3
    min_time_limit = 2
    while lives > 0:
        minigame_index = remaining_minigame_indices.pop()
        minigame_func, minigame_label = minigames[minigame_index]
        clear()
        print(f"Playing: {minigame_label}")
        success = call_minigame(minigame_func, time_limit=current_time_limit)
        if success:
            score += 1
            print(f"✅ Success! Score: {score} ⭐")
            # If cruel mode is on, gradually reduce the time limit to make the game harder
            if cruel_mode and score % cruel_decrement_every == 0 and current_time_limit > min_time_limit:
                current_time_limit -= 1
                print(f"⚠️ Time limit decreased! New limit: {current_time_limit}s")
        else:
            lives -= 1
            print(f"💔 Oops! Lives left: {hearts_display(lives)}")
        input("Press ENTER to continue...")
        if not remaining_minigame_indices:
            remaining_minigame_indices = list(range(len(minigames)))
            random.shuffle(remaining_minigame_indices)
    return score


def main():
    """
    Main game loop: shows menu, handles user choices, and manages difficulty.
    """
    print("DUMB WAYS TO DIE — Main Game Launcher")

    minigame_functions = discover_all()
    if not minigame_functions:
        print("No minigames found. Verify MINIGAME_MODULE_FILES list and that files exist.")
        sys.exit(1)

    # Build game list and main menu
    minigame_labels = [minigame_label for (_, minigame_label) in minigame_functions]
    MAIN_MENU_OPTIONS = ["Start Game (randomized)", "Play Single Minigame", "Difficulty", "Toggle Cruel Mode", "View Credits", "Quit"]
    # default difficulty
    difficulty = "Normal"
    time_limit_by_difficulty = {
        "Easy": 20,
        "Normal": 12,
        "Hard": 8,
    }
    global_time_limit = time_limit_by_difficulty[difficulty]
    is_cruel_mode = False

    while True:
        clear()
        print("Dumb Ways to Waterloo — Main Menu\n")
        for i, option in enumerate(MAIN_MENU_OPTIONS, start=1):
            if option == "Difficulty":
                print(f" [{i}] {option} (current: {difficulty})")
            elif option == "Toggle Cruel Mode":
                print(f" [{i}] {option} (current: {'ON' if is_cruel_mode else 'OFF'})")
            else:
                print(f" [{i}] {option}")
        print()
        # show current cruel mode when choosing from the menu
        selected_option = get_choice(len(MAIN_MENU_OPTIONS))
        if selected_option is None:
            print("Please choose a number.")
            input("Press ENTER to continue...")
            continue

        menu_selection = MAIN_MENU_OPTIONS[selected_option - 1]
        if menu_selection == "Quit":
            print("Thanks for playing — bye! 👋")
            break

        if menu_selection == "Start Game (randomized)":
            lives = 3
            print(f"Starting Game (randomized) with {lives} lives {hearts_display(lives)} — time limit: {global_time_limit}s — good luck!")
            score = play_survival(minigame_functions, lives, time_limit=global_time_limit, cruel_mode=is_cruel_mode)
            # show the final score when the player loses all lives
            print(f"\n☠️  Game over! Final score: {score}")
            # Check high score
            old_high_score = read_high_score()
            if score > old_high_score:
                print(f"🎉 New high score! Old: {old_high_score}, New: {score}")
                save_high_score(score)
            else:
                print(f"High Score: {old_high_score}")
            input("Press ENTER to return to menu...")
            continue

        if menu_selection == "Play Single Minigame":
            # Show minigame list
            while True:
                clear()
                print("Select a minigame to play:\n")
                for i, minigame_label in enumerate(minigame_labels, start=1):
                    print(f" [{i}] {minigame_label}")
                print()
                minigame_choice = get_choice(len(minigame_labels))
                if minigame_choice is None:
                    print("Please choose a number.")
                    input("Press ENTER to continue...")
                    continue
                minigame_func, minigame_label = minigame_functions[minigame_choice - 1]
                play_single_game(minigame_func, minigame_label, time_limit=global_time_limit)
                break
            continue

        if menu_selection == "Difficulty":
            # difficulty menu
            while True:
                clear()
                print("Select difficulty:\n")
                for i, difficulty_label in enumerate(["Easy", "Normal", "Hard", "Custom"], start=1):
                    print(f" [{i}] {difficulty_label}")
                print()
                difficulty_choice = get_choice(4)
                if difficulty_choice is None:
                    print("Please choose a number.")
                    input("Press ENTER to continue...")
                    continue
                if difficulty_choice == 4:
                    # custom
                    val = input("Enter time limit per minigame in seconds (e.g., 8):").strip()
                    if not val.isdigit() or int(val) <= 0:
                        print("Invalid input, must be positive integer")
                        input("Press ENTER to continue...")
                        continue
                    global_time_limit = int(val)
                    difficulty = f"Custom ({global_time_limit}s)"
                else:
                    difficulty = ["Easy", "Normal", "Hard"][difficulty_choice - 1]
                    global_time_limit = time_limit_by_difficulty[difficulty]
                print(f"Difficulty set to {difficulty} (time limit {global_time_limit}s)")
                input("Press ENTER to continue...")
                break
            continue
        if menu_selection == "Toggle Cruel Mode":
            is_cruel_mode = not is_cruel_mode
            state = "ON" if is_cruel_mode else "OFF"
            print(f"Cruel Mode: {state}. Time limit will {'shrink' if is_cruel_mode else 'stay fixed'} during survival.")
            input("Press ENTER to return to menu...")
            continue

        if menu_selection == "View Credits":
            clear()
            print("Dumb Ways to Waterloo — Credits\n")
            print("Game concept: Dumb Ways to Die parody for CHE-120\n")
            print("Contributors: Sarah, Madi, Katie, and Krist!\n")
            print("Special thanks to our CHE120 professor Pendar Mahmoudi for her guidance and this opportunity.\n")
            print("And to GitHub Copilot for code suggestions!\n")
            print("Python CLI game by Waterloo students, 2025.\n")
            input("Press ENTER to return to menu...")
            continue


if __name__ == "__main__":
    main()
 
