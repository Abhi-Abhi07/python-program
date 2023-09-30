totalBike=100
price=10
while 1:
    print("""
        1. Display Available Bike
        2. Request a bike for rent(100 Rs -> Qty
        3. Exit
        """)
    a=int(input(   ))
    if a==1:
        print("Total available stocks:- ",totalBike)
    elif a==2:
        qty=int(input("Enter the Qty would you like to rent :--- "))
        if totalBike>=qty:
            totalBike=totalBike-qty
            print("Total Price",qty*price)
            print("Total Available stock:- ",totalBike)
        else:
            print("Sorry! We currently",totalBike,"bikes available to rent")
            print("Total price ",totalBike*price)
    elif a==3:
        break
    else:
        print("Invalid choice")