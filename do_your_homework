import time
import os

HOMEWORK_PICS = ['''
|           |
|           |
|           |
|           |
|           |
|           |''', '''

|  CHE 100  |
|           |
|           |
|           |
|           |
|           | ''', '''

|  CHE 100  |
|  CHE 102  |
|           |
|           |
|           |
|           |''','''

|  CHE 100  |
|  CHE 102  |
|  CHE 120  |
|           |
|           |
|           |''','''

|  CHE 100  |
|  CHE 102  |
|  CHE 120  |
|  CHE 180  |
|           |
|           |''','''

|  CHE 100  |
|  CHE 102  |
|  CHE 120  |
|  CHE 180  |
|  MATH 116 |
|           |''','''

|  CHE 100  |
|  CHE 102  |
|  CHE 120  |
|  CHE 180  |
|  MATH 116 |
|  MATH 115 |'''
]

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def do_your_homework():
    print('Quick you have 5 seconds to finish your homework!')
    time.sleep(2)

    start_time = time.time()
    
    for pics in HOMEWORK_PICS:
        clear_screen()
        print(pics)
        input('Click ENTER until you finish all your homework:')
    
        if time.time() - start_time >= 5:
            clear_screen()
            print(pics)
            print("\n TIME'S UP! You didn’t finish all your homework!")
            return

    clear_screen()
    print(HOMEWORK_PICS[-1])
    print("\n CONGRATS! You finished your homework in time (this time)")
    
do_your_homework()
