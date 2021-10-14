# sasha motlagh
# 10/7/21
# learning how to:
# open() open a File
# write to a File 'w'
# read from a File 'r'
# append to a File 'a'
    #add at the end instead of change
# close() close a File 
import os, time
#to create a file you must declare an object so we can open a file
#when you open a file for the first time you need to use 'w'
myFile= open('score.txt','w')
myFile.write("hello there, my name is sasha\n what is yours?")
myFile.close()
#always close a file when you're done using it
myFile=open('score.txt','w')
myFile.write("and now we will play a game")
myFile.close()

fileMy=open('score.txt','r')
fileMy.write("awkward")
print(fileMy.read())
fileMy.close()

score=450
anotherFile=open('score.txt','a')
anotherFile.write("\nThe highest score: \t"+ str(score))
anotherFile.close()