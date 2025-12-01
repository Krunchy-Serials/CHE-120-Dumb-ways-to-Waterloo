ALIVE_BLOB = [
    "   .------.   ",
    "  /        \\  ",
    " |   O   O  | ",
    " |          | ",
    " |   ----   | ",
    "  \\        /  ",
    "   '------'   "
]

DEAD_BLOB = [
    "   .------.   ",
    "  /        \\  ",
    " |   x  x   | ",
    " |          | ",
    " |   ----   | ",
    "  \\        /  ",
    "   '------'   "
]








import time
import random
import threading

def print_blobs(lives):
    """Prints 3 blobs in a row, updating for dead/alive blobs."""
    blob_list = []
    for i in range(3):
        if i < lives:
            blob_list.append(ALIVE_BLOB)
        else:
            blob_list.append(DEAD_BLOB)

    
    for line_idx in range(len(ALIVE_BLOB)):
        print("   ".join(blob[line_idx] for blob in blob_list))
   


def timed_input(prompt, timeout):
    user_input = [None]

    def get_input():
        user_input[0] = input(prompt)

    thread = threading.Thread(target=get_input)
    thread.daemon = True
    thread.start()

    thread.join(timeout)
    return user_input[0]  # returns None if time expired


# Minigames!!!

def minigame_wrong_subject(time_limit=None):
    effective_time = time_limit or 7
    print(f"\n💣 QUICK! Choose the subject that doesn't fit before the bomb blows! ({effective_time}s)")
    print("Type: CHE120 / CHE100 / MATH100")
    answer = timed_input("Your choice: ", effective_time)

    if answer == "MATH100":
        print("✅ Correct! We don't take MATH100")
        return True
    else:
        print("💥BOOM! You take this class!!(you should know what courses you take...")
        return False


def minigame_fail_exam(time_limit=None):
    # Give more time for this minigame; default to 20s unless the difficulty overrides it.
    effective_time = time_limit or 20
    print(f"\n 💬 TYPE FAST! Type the sentence 'input-output+generation-accumulation=0' within {effective_time} seconds to not fail your exam!")
    answer = timed_input("Type here: ", effective_time)

    if answer == "input-output+generation-accumulation=0":
        print(" Nice, you didn't fail!😎")
        return True
    else:
        print("⏱️ Too slow or wrong, you failed your exam🫣!")
        return False


    
def minigame_math(time_limit=None):
    effective_time = time_limit or 3
    print(f"\n🧮 Solve this FAST or Professor Comfort will smack you: derivative of x^2+3 = ? ({effective_time} seconds)")
    answer = timed_input("Your answer: ", effective_time)

    if answer == "2x":
        print("👍 Correct! Professor Comfort is Happy, Happy, Happy")
        return True
    else:
        print("❌ Times up! You should've studied more...😬")
        return False

def minigame_tims_run(time_limit=None):
    effective_time = time_limit or 15
    print(f"\n☕️ You're running late to class but also need caffeine — type 'LARGE ICED COFFEE' in {effective_time} seconds to order as fast as you can!")
    answer = timed_input("Type here: ", effective_time)

    if answer == 'LARGE ICED COFFEE':
        print("Your addiction was fed, and you made it to class!⚡️")
        return True
    else:
        print("Too slow! You waited in line for 20 min and were late to class")
        return False
       
    
if __name__ == "__main__":
    main()

