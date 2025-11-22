#This chapter coves something I learnt in C#/Javascript, which is input and functions

def flop_assigner(question):
    answer = input(question)
    print(answer,"flopped, but anyways...")
    print()
    return answer

diva_1 = flop_assigner("What is your pop diva? ")

diva_2 = flop_assigner("Who is your top 1 on spotify? ")

import random

def diva_chooser(diva_1,diva_2):
    divas = [diva_1,diva_2]
    return random.choice(divas) + " outsold"

print(diva_chooser(diva_1,diva_2))