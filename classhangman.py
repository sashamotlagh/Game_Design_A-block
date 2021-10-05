#sasha motlagh
#hangman class code

import os
import random
def updateword(word, guesses):
    for letter in word:
        if letter in guesses:
            print('_', end=' ')

def menu():
    print("#########################################")
    #put instructions here
    print("#                  menu                 #")
    print("                                         ")
    print("       1 baking ingredients              ")
    print("       2.animals                         ")
    print("       3.fruits                          ")
    print("       4.exit                            ")
    print("to play game select 1-3, to exit select 4")
    print("#########################################")
    sel=input("What would you like to do?")
    #check for integer
    sel=int(sel)
    return sel
def selword(sel):
    if sel == 1:
        word=random.choice(bakinging)
    elif sel==2:
        word=random.choice(animals)
    elif sel ==3:
        word=random.choice(Fruits)
    return word

animals=["tiger", "sloth","dolphin"]
Fruits=["banana","pinneapple","orange","strawberry"]
bakinging=["flour","egg","sugar","milk","butter","cream"]
name= input("what is your name?")

counter=0
sel=menu()
while sel !=4:
    print(name+" Good luck you have 5 chances :)")
    turns=5
    counter+=1
    word=selword(sel)
    word=word.lower()
    wordcount=len(word)
    letcount = 0
    print(word) #checking code
    guesses=''
    updateword(word, guesses)

    while turns>0 and letcount<=wordcount:
       newguess=input(name+" give me a letter")
    if newguess in word:
            guesses+=newguess
            print("you guessed one")
    else:
            turns-=1
            print("sorry, you have ", turns, " turns left")
    updateword(word, guesses)
os.system('cls')
sel=menu()
