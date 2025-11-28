# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 16:58:03 2025

@author: kkurt
"""
import random 

wrong_choices = ['scream as loud as you can', 'climb out of the emergency trap door', 'cry', 'call your mom','summon a goose to help you','jump', 'pry open the door','use mass balances', 'make a titration out of your tears', 'wipe your tears with your 102 midterm', 'meditate', 'write a lab report on your experimental findings']

right_choices = ['study for your linear algebra exam! Theres no time to lose!', 'press the emergency button', 'Apply Le Chatelier’s Principle to reduce stress', 'wait for help to arrive', 'hack into the elevator mainframe (launch jupyter notebook)']

def getrandomword(choiceList):
    Index = random.randint(0, len(choiceList) - 1)
    return choiceList[Index]

def escape_dana_porter_elevator():
    
    print('quick! You are stuck in the Dana Porter Elevator! Choose your escape wisely \n')
    
    correct = random.choice(right_choices)
    
    incorrect = random.sample(wrong_choices, 2)

    options = [correct] + incorrect
    random.shuffle(options)
    
    for i, choice in enumerate(options, start=1):
        print( str(i) + ". " + str(choice))
    
    while True:  
        answer = input('\n please pick your answer (1-3):')
   
        if not answer.isdigit() or int(answer) not in [1,2,3]:
            print('looks like this will take a while! Choose a valid input to escape the elevator!')
            continue
        
        break

    validated_input = int(answer)
    selected = options[validated_input - 1]
    
    if selected in right_choices:
        print('Congrats! You have escaped the Dana Porter Elevator')
    else:
        print('FAIL! You are forever stuck in the elevator')
    

escape_dana_porter_elevator()
