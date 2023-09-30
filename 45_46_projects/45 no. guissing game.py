import random

x=random.randrange(1,101)

# print(x)

atm=1
while 1:
    n = int(input("Enter number : "))
    if n > x:
        print("Enter lesser number")
        atm=atm+1
    elif n < x:
        print("Enter greter number")
        atm=atm+1
    else:
        print("you will win of ",atm," atempt")
        exit(0)