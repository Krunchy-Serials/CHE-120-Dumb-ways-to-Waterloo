
import random

def exam_room(player=None):
    print("\n PAC EXAM ROOM\n")
    print("  [1]   [2]   [3]")
    print()

def find_exam_desk(time_limit=None):
    print("\nFind your exam desk! BEWARE, its nesting season!\n")
    
    correct = random.randint(1, 3)

    while True:
        exam_room()

        answer = input("Choose your desk (1–3): ")

        if not answer.isdigit() or int(answer) not in [1, 2, 3]:
            print("Invalid input. Hurry to find you seat before the exam starts.\n")
            continue

        answer = int(answer)

        if answer == correct:
            exam_room(player=answer)
            print("\n [✔] You found your correct exam desk! Good luck!")
            return True
        else: 
            print("\n   [🦆]  HONK!! Wrong desk!!")
            return False

if __name__ == "__main__":
    find_exam_desk()