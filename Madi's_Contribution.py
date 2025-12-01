
import time
import random
import threading

def timed_input(prompt, timeout):
    user_input = [None]

    def get_input():
        user_input[0] = input(prompt)

    thread = threading.Thread(target=get_input)
    thread.daemon = True
    thread.start()

    thread.join(timeout)
    return user_input[0]


# Game Ideas
#MS this fuction is about closing the fume hood, you have to type "close" before the time runs out. 
#MS If the input does not match, the code returns false and prints the message attached to the false if statement. 
#MS If the input matches exactly then the function returns true and it prints the statement associated with the true if statement.
def close_fume_hood(time_limit=None):
    effective_time = time_limit or 10
    print(f"\n🚨QUICK! Type 'close' to close the fume hood ({effective_time}s) 🚨")
    answer = timed_input('\ntype here: ', effective_time)
    
    if answer == 'close':
        print('you saved the lab!! 😅')
        return True
    else:
        print('everyone is unconscious...')
        return False

#MS this function is about the learn site crashing, you have to type "submit" before the time runs out.
#MS If the input does not match exactly then the function goes to the else statement and prints the statement associated, and returns false.
#MS If the input matches exactly then the function goes to the if statement and prints the statement associated, and returns true
def learn_crash(time_limit=None):
    effective_time = time_limit or 10
    print(f"\nLearn is crashing and the assignment is due!! 💻 ({effective_time}s)")
    print('\ntype \'submit\' as quick as you can!!')
    answer = timed_input('\ntype here: ', effective_time)
    
    if answer == 'submit':
        print('just in time, 55%!! 😅')
        return True
    else:
        print('another failed assignment...')
        return False

#MS this function is a multiple choice question. This question tests the users lab skills.
#MS if the input does not match the exactly the function returns false and prints the statement associated.
#MS if the input does match exactly then the function returns true and prints the statement associated
def meniscus_dilemma(time_limit=None):
    effective_time = time_limit or 10
    print(f"\nthe meniscus in the beaker is too high, what do you do? 🧪 ({effective_time}s)")
    print('\n1) add more \n2) use your mouth and blow it out \n3) remove a drop with a pipette')
    answer = timed_input('\ntype here: ', effective_time)
    
    if answer == '3':
        print('perfect!')
        return True
    else:
        print('have you done your safety? 🤔')
        return False

#MS although we don't have a reactor at the university, this could be a career branch for some of us. the user has to type the code before time runs out
#MS if the input does not match exactly then the function goes to the else statement and returns false and prints the statement associated
#MS if the input does match exactly then the function goes to the if statement and returns true and prints the statement associated
def reactor_leak(time_limit=None):
    codes = ['A57JP', 'J9OW1', 'NA7T1', '94RU2', 'NI218', '36KQ0']
    effective_time = time_limit or 10
    print(f"\nQUICK! Type the code so the reactor is fixed ({effective_time}s)")
    code = random.choice(codes)
    print(code)
    answer = timed_input('\ninput code: ', effective_time)
    
    if answer == code:
        print('thank goodness you stopped the leak')
        return True
    else:
        print('\nWere those fish green before...')
        return False
    
MINIGAMES = [close_fume_hood, learn_crash, meniscus_dilemma, reactor_leak]
