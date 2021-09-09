#sasha motlagh
#
import os

os.system('cls')
star=int(input("how many stars?"))
print("stars", star)
line=star
for i in range(line):
    #add a loop for the spaces
    for space in range(i):
        print(" ", end=" ")
    for counter in range(star): #you can use a number or variable
        print("*", end=" ")
        #print(counter+1, end=" ")
    print() #print a return creating a new line
    #shortcut for star=star-1
    star-=1
print("Thank you! ")
