# sasha motlagh
# data types
userinput=input("type something")
print(type(userinput))
try:
    int(userinput)
    check=True
except ValueError:
    check=False

if(check):
    print()
else:
    print(len(userinput))
for i in userinput:
    print(i)

if len(userinput>3):
    print(userinput[3])
