# CHE-120: Dumb Ways to Waterloo

This repository contains a collection of small, text-based minigames grouped
into a single launcher called `Main_Game.py`. The intent is educational — this
project is ideal made by college students learning Python, and each minigame is a
simple interactive exercise showcasing functions, input handling, timing, and
dynamic module loading. The launcher also shows simple emoji feedback and
tracks a persistent high score in `highscore.txt`.

Contents
--------
 - `Main_Game.py`: simplified game launcher — choose and play a minigame or play
	 Survival Mode. The launcher includes a menu to:
	 - Start Game (randomized)
	 - Play a single minigame
	 - Change difficulty
	 - Toggle Cruel Mode (cause time limits to shrink during survival)
	 - View credits
- `Safety_Inspection_Minigame.py`: one-question safety hazard game.
- `do_your_homework.py`, `find_exam_desk.py`, `dana_porter_elevator.py`: theme
	“campus” minigames.
- `Sarah V1.py`, `Madi's_Contribution.py`: multiple small minigames / challenges.

Basic idea
----------
Each minigame is a small Python function that asks the user to type or select a
choice and returns either `True` (success) or `False` (failure). The `Main_Game`
launcher imports these functions and lets players pick a minigame to run or run
a random survival sequence where minigames are played until lives are gone.

How to run
----------
Open a terminal, `cd` into the repo root, then run:

```bash
python3 Main_Game.py
```

Main Menu & Difficulty
----------------------
When you start the game, a simplified main menu will appear. The menu lets you:

 - Start Game (randomized): the minigames will automatically be played in a
	 randomized order; you will have a number of lives and the game proceeds until
	 you lose your lives. If "Cruel Mode" is enabled, the per-minigame time limit
	 will decrease as you rack up successful wins, so the game gets harder the
	 better you do.
 - Difficulty: choose from Easy / Normal / Hard or a Custom time limit; this sets
	 the number of seconds many minigames will allow for responses.
	Each minigame will display the effective time for its prompt so the player knows
	how long they have.
  
- Quit: exit the launcher.
Safety Inspection
-----------------
Safety Inspection now shows a single random hazard per invocation but always
presents 3 options; choose one to respond. The `Safety_Inspection_Minigame` is
designed to be safe and educational and follows the `time_limit` convention.
It returns True/False like the other minigames.


How minigames should be implemented
----------------------------------
Keep the API very simple so other students can add minigames easily.

- Preferred: module exports a list called `MINIGAMES` — e.g.
	```python
	def my_minigame(time_limit=None):
			# ... interactive prompt
			return True  # if succeeded

	MINIGAMES = [my_minigame]
	```
- Or export a single function called `run(time_limit=None)` or a logically
	named function like `do_your_homework(time_limit=None)`.
- All minigame functions should accept an optional `time_limit` parameter and
	return a boolean value (True/False), and be tolerant of `time_limit=None`.

How to add a minigame (step-by-step)
-----------------------------------
1. Create a new file, e.g. `my_minigame.py`.
2. Add a `MINIGAMES` list with one or more functions (see example above), or
	 add a single `run(time_limit=None)` function.
3. Add your file to `MINIGAME_FILES` in `Main_Game.py` (the short list at the
	 top of the file). The launcher will pick it up automatically.

Tips for keeping it simple
-------------------------
- Avoid complex data structures; focus on `input`, `print`, and simple logic.
- Use `time.sleep()` sparingly (it's ok for simple delays) — but prefer using
	`threading` and/or `input` timeouts sparingly.
- Keep the function small and readable; if you copy an existing minigame,
	follow its structure and replace text/logic as needed.

- Want to extend it?
------------------
- This launcher optionally records a persistent integer high score in
	`highscore.txt` (next to `Main_Game.py`). You can also instead store a
	JSON structure if you prefer. See `Main_Game.py` for the exact file used.
- Build a `minigames/` package if the number of files grows too large.
- Add tests for `Main_Game.collect_minigames()` and `call_minigame()` so future
	contributors don't cause regressions.

License & credits
-----------------
This is a student project — no license is attached by default. Credit any
contributor(s) for their minigames in the code comments.

Enjoy! 🎮
