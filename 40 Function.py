def simpleFun():
    print("Ai is Ab")


def addToNum(a,b):
    print(a+b)


def subToNum(a,b=10):
    return a-b


simpleFun()
simpleFun()
simpleFun()
i=18
j=5
addToNum(i,j)
print("calling sub fun : ",subToNum(i))
print("calling sub fun : ",subToNum(i,j))
