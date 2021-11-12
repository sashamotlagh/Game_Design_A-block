#operators
#arithmetic operators
# + - * / %
# % gives remainder and if there is none it equals zero
#check for even numbers
# %=mod
import os
os.system('cls')

num= int(input("give me a number"))
#rem=num%2
#conditional
#if(rem== 0): #equals by default assigns value to variable, 2 equals asks instead of define
    #print("the number is even")
#else:
    #print("the number is odd")
#find the last number, second last, and third last numbers (challenge)
rem=num
if(rem==num):
    print(rem%10)
else:
    print("fail")

if(rem==num):
    print(rem%100)
else:
    print("fail")

if(rem==num):
    print(rem%1000)
else:
    print("fail")