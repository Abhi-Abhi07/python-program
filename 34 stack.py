l=[]
while True:
    i=int(input('''
        1. push element
        2. pop element
        3. peek element
        4. Diplay Stack
        5. exit
        
        '''))
    if i==1:
        e=input("Enter element you want to push :- ")
        l.append(e)
        print(l)
    elif i==2:
        if(len(l)==0):
            print("Empty Stack !")
        else:
            l.pop()
            print(l)
    elif i==3:
        if(len(l)==0):
            print("Empty Stack !")
        else:
            print("Last Stack Value :- ",l[-1])
    elif(i==4):
        print("Displaying Stack :-) ",l)
    elif(i==5):
        break
    else:
        print("Invalid Operation !")
