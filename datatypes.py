# sasha motlagh
import os

os.system('cls')
userInput=input("type something ")
print (type(userInput))

try:
    userInput=int(userInput)
    check=True

except ValueError:
    check=False

if(check):
    #I will be back
    print(userInput+7)
else:
    print(len(userInput))
    for i in userInput:
        print(i,end='')
    print()
    if (len(userInput)>3):
        print (userInput[3])



# This is about data Type

# how strings work