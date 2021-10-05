#sasha motlagh
#hangman class code

import os
import random
os.system('cls')
def updateword(word, guesses):
    for letter in word:
        if letter in guesses:
            print(letter, end=' ')
        else:
            print('_',end=' ')
            

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
bakinging=["flour","nuts","sugar","milk","oil","cream"]
name= input("what is your name?")

counter=0

sel=menu()
while sel !=4:
    print(name+" Good luck you have 5 chances :)")
    counter=0
    word=selword(sel)
    word=word.lower()
    wordcount=len(word)
    letcount = 0
    turns=5
    print(word) #checking code
    guesses=''
    updateword(word, guesses)
    newguess=''
    while turns>0 and counter<=len(word):
        print()
        newguess=input(name+" give me a letter")
        if newguess in word:
            guesses+=newguess
            print("you guessed one")
            counter+=1
        else:
            turns-=1
            print("sorry, you have ", turns, " turns left")
        updateword(word, guesses)
    if turns == 0:
        print("you lost")
    else:
        print("you won")

    sel=menu()
print("Thank you for playing")