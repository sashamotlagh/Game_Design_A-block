#sasha motlagh
#hangman class code

import os
import random

bakinging=["flour","egg","sugar","milk","butter","cream"]
print("word game")
print("guess the baking ingredient i am thinking of")
name= input("what is your name?")
counter=0
answer= input(name+" do you want to play?")
while 'y' in answer: #control the number of games
    print(name,+" Good luck you have 5 chances :)")
    turns=5
    counter+=1
    word=random.choice(bakinging)
    print(word) #checking code
    guesses=''
    for letter in word:
        if letter in guesses:
            print(letter,end=" ")
        else:
            print("_",end=" ")
    while turns>0:
       newguess=input(name+" give me a letter")
    if newguess in word:
            guesses+=newguess
            print("you guessed one")
    else:
            turns-=1
            print("sorry, you have ", turns, " turns left")
er=input(name,)