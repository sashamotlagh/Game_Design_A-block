#sasha motlagh
#hangman class code

import os
import random
print("Hello")

def updateword(word, guesses, letCount): #updating the word throughout the game for points
    for letter in word:
        if letter in guesses:
            print(letter, end=' ')
            letCount+=1
        else:
            print('_',end=' ')  
    return letCount   
def menu():
    print("#########################################")#put instructions here
    print("#                  menu                 #")
    print("                                         ")
    print("       1 baking ingredients              ")
    print("       2.animals                         ")
    print("       3.fruits                          ")
    print("       4.scoreboard                      ")
    print("       5.exit                            ")
    print("to play game select 1-3, to exit select 5")
    print("#########################################")
    sel=input("What would you like to do?")
    #check for integer
    sel=int(sel)
    return sel
def selword(sel): #picking which part of the game is being played
    if sel == 1:
        word=random.choice(bakinging)
    elif sel==2:
        word=random.choice(animals)
    elif sel==3:
        word=random.choice(Fruits)
    return word
name=input("what is your name?") 
#the options for words based on the category
animals=["tiger", "sloth","dolphin","penguin","kangaroo","bear","horse"]
Fruits=["banana","pinneapple","orange","strawberry","mango","kiwi","grape"]
bakinging=["flour","nuts","sugar","milk","oil","cream","egg"]
score=0  #store current score
maxscore= 0 #store highest score
counter=0 #keeps track of letters
def scoreBoard(): #reading the scoreboard file to the player and updating it
    myFile=open('scoreboard.txt','r')
    print(myFile.read())
    myFile.close()
def exitNow():#function for keeping and appending the highscore within the txt file for the end of the game
    myFile=open('scoreboard.txt','a')
    myFile.write('\n'+ name + "\t Highest score: "+str(maxscore)+'\n')
    myFile.close()
    print("Thank you for playing")
def checkExit(sel): #based on selection the scoreboard will print or the game will end
    if sel==4:
        scoreBoard()
        sel=menu()
    if sel==5: 
        exitNow()  
sel=menu()
checkExit(sel)
while sel <4: #the game option regardless of the category it will run with 5 chances per word
    print(name+" good luck you have 5 chances :)")
    counter=0
    word=selword(sel)
    word=word.lower()
    wordCount=len(word)
    letCount = 0
    turns=5
    print(word) #checking code
    guesses=''
    updateword(word, guesses, letCount)
    newguess=''
    while turns>0 and letCount<wordCount: #while loop for keeping the words separated between tries
        print()
        newguess=input(name+" give me a letter")
        if newguess in word:
            guesses+=newguess
            print("you guessed one")
        else:
            turns-=1
            print("sorry, you have ", turns, " turns left")
        letCount=0
        letCount= updateword(word, guesses,letCount)
    print()
    score=3*wordCount+5*turns #calculating the score based on how well the player did
    if score>maxscore:
        maxscore=score
    else:
        maxscore=maxscore #doesn't change if it's not higher
    sel=menu()
    checkExit(sel) 