
import os
import random
 
name = input("what is your name? ")
 
print("Good Luck ! ", name)
print("you have 11 tries since there are 11 posibilities")
 
words = ['giraffe', 'tiger', 'sloth', 'cat',
         'python', 'tiger', 'dog', 'zebra',
         'deer', 'panda', 'boar', 'horse']


while 'y' in input("do you want to play a game"):
    word = random.choice(words)
    word=(word.lower())
    print(word)
    turns=11
    while turns > 0:
        guess= input("Guess the animal")
        guess=(guess.lower())
        if (guess==word):
            print(word)   
            print("you win")
            turns=-1
        else:
            print("is not correct")
            turns-= 1
        
    print("would you like to play again?")
print("good game")