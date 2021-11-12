#sasha motlagh random words game

import random
flag=True

answer=input ("what animal am i thinking of?")
while myanimals in answer:
    animals=['horse','python','tiger','boar','dear']
    myanimals= random.choice(animals)
    counter=5
    while (flag and counter>True):
        if input in myanimals:
            input==myanimals
            print("you won")
        else:
            counter-=1
            print("do you want to try again?")
            if 'y' in input:
