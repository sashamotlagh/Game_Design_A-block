#combined looping
star=int(input("how many stars?"))
stars2=star 
print("stars", star)
line=star
space=0

for i in range(line):
    for counter in range(star):
        print("*", end=" ")
    star-=1
    
    for j in range(space):
        print(" ", end=" ")
    space+=2

    for counter in range(stars2):
        print("*", end=" ")
    
    print()
    stars2-=1 