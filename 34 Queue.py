l=[]
while True:
    i=int(input("""
            1. push element
            2. pop First element
            3. Front element
            4. Last element
            5. Dispaly queue
            6. exit
            
            """))
    if i==1:
        n=int(input("Enter value : "))
        l.append(n)
        print(l)
    elif i==2:
        if len(l)==0:
            print("queue is empyt")
        else :
            del l[0]
            print(l)
    elif i==3:
        if len(l)==0:
            print("queue is empty")
        else :
            print("First elment",l[0])
    elif i==4:
        if len(l)==0:
            print("Empty queue")
        else :
            print("last element ",l[-1])
    elif i==5:
        print("Displaying list : ",l)
    elif i==6:
        break
    else :
        print("intvalid opr...")



