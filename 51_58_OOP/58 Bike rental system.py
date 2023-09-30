class bikeShop:
    def __init__(self,stock):
        self.stock=stock
    def displaybike(self):
        print("Total Bikes",self.stock)

    def rentForBike(self,q):
        if(q<=0):
            print("Enter the positive value or greter then zero")
        elif q>self.stock:
            print("Enter the value (less then stock)")
        else:
            self.stock = self.stock - q
            print("Total Price",q*10)
            print("Total Bike",self.stock)


while 1:
    obj=bikeShop(100)
    uc=int(input("""
    1.display stocks
    2.Rent a bike
    3.Exit
    """))
    if uc==1:
        obj.displaybike()
    elif uc==2:
        n=int(input("Enter the qty:---"))
        obj.rentForBike(n)
    else:
        break