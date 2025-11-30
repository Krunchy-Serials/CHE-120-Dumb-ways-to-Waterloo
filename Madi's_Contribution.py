
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
