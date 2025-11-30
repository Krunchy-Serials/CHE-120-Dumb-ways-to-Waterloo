import random
import time

def safety_inspection_minigame(time_limit=None):
    
    
    
    print("\n=== SAFETY INSPECTION MINIGAME ===")
    print("Respond with the safest action for each hazard.\n")
    
    if time_limit:
        print(f"WARNING: You have {time_limit} seconds per question!\n")
        
    hazards = [
        {
            "hazard": "Your friend is not wearing goggles while handling chemicals.",
            "options": [
                "Tell them to put on their goggles immediately.",
                "Take off yours too so it's fair.",
                "Pretend you didn't see it."
                ],
            "correct":"1"
        },
        {
            "hazard": "Someone left an open bottle of Concentrated Acid on a stool.",
            "options": [
                "Leave it. Someone else probably needs it soon.",
                "Clean the container and clean up any spills.",
                "Smell it to identify the acid."
                ],
            "correct":"2"
        },
        {
            "hazard": "The emergency shower is blocked with lab stools.",
            "options": [
                "Move the stools away immediately.",
                "Sit on the stools because you're tired.",
                "Ignore it. No one uses the safety showers anyway."
                ],
            "correct":"1"
        },
        {
            "hazard": "There is broken glass near the sink.",
            "options": [
                "Push it away so no one using the sink gets cut.",
                "Throw it away in the regular garbage.",
                "Pick it up with gloves or tongs and dispose in glass waste."
                ],
            "correct":"3"
        },
        {
            "hazard": "A Bunsen Burner is left on with no supervision.",
            "options": [
                "Extinguish it and notify the TA or Professor.",
                "Turn the gas up cuz fire iz COOL.",
                "Ignore it and hope that it goes out on its own."
                ],
            "correct":"1"
        },
        {
            "hazard": "!!!THE LAB IS ON FIRE!!!",
            "options": [
                "This is fine. I like the warmth.",
                "AAAHHHHH!!! RUN FOR YOUR LIVESSSS!!!",
                "Pull the fire alarm, inform authorities, and exit in an orderly manner."
                ],
            "correct":"3"
        },
        {
            "hazard": "You acidentally weighed too much solute",
            "options": [
                "Put the solute in the solvent anyways. It won't affect the yield that much",
                "Remove the excess solute and dispose of it properly",
                "Put the solute back in the container. They'll never know."
                ],
            "correct":"2"
        }
        ]
    # Ask just one random hazard per run
    h = random.choice(hazards)
    print(f"\nHazard: {h['hazard']}\n")
    for i, option in  enumerate(h["options"], start=1):
        print(f" {i}) {option}")

    # ---- Ask the user ----
    start_time = time.time()
    choice = input("\nYour Answer:\t")

    # Processing Player Input
    try:
            if time_limit is not None and (time.time() - start_time) > time_limit:
                print("\nTime's Up! Your indecision during a hazard is unsafe by default.")
                return False
            # Validate digit choice
            if not choice.isdigit() or int(choice) not in range(1, len(h['options'])+1):
                print("\nInvalid Input! This is counted as unsafe.")
                return False
            if choice == h["correct"]:
                print("\nCorrect! Your knowledge of safety saved the day.")
                return True
            else:
                print("\nIncorrect! You picked an Unsafe choice.")
                return False
    except ValueError:
            print("\nInvalid Input! This is counted as unsafe.")
            return False
            
    # should be unreachable as this function returns after the single question
    return False
                

if __name__ == "__main__":
    print("Starting \"Safety Inspection\" Minigame Playtest")
    total = 0
    for _ in range(5):
        if safety_inspection_minigame(time_limit=10):
            total += 1
    print("Total correct:", total)
    
