#sasha motlagh
import os
import random
num="h"
answer = input("Do you want to play a game")
while ('y' in answer):
    randy=random.randint(1,100)
    chances= 0
    print("welcome")
    print(randy)
    while (chances<10 and num!=randy):
        num= input("give me a number")
        try:
            num=int(num)
            chances+=1
            if num==randy:
                print("you win :)")
            else:
                print("try again")
        except ValueError:
            check=False
            print("guess an integer")
    answer=input("do you want to play again")
