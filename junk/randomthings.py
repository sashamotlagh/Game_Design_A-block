#sasha motlagh
#how to use random numbers
#make a guessing number game

import os
import random
#this for loop was to play with random numbers
random.seed(20)
for i in range(10):
    randy=random.randint(3,5)
    print(randy)
    randy2=random.random()
    randy2*=100
    print(int(randy2))
#arrays in python are called lists
fruits=["strawberry","bluebarry","banana","apple"]
myfruit= random.choice(fruits)
print(myfruit)


