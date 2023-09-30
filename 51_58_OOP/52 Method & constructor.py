class Ai:
    a=10
    b=20

    # creating constructor
    # object creating ke time automatic call hota hai
    def __init__(self):
        print("Ai is Abhi")

    # self ki jagah koi bhi name use kar sakte hai & it is madatary
    # use class ke data ko access karne ke liye
    def showValue(self):
        print(self.a)

    def showValue1(this):
        print(this.a)

    # with self class wale argument consider hote hai
    # a=10
    # b=20
    def sum(self,a,b):
        self.s=self.a+self.b
        print(self.s)

    # without self jo argument object ke throw pass kiye wo consider hote hai
    # a=2
    # b=3
    def sum2(self,a,b):
        s=a+b
        print(s)

A=Ai()
A.showValue()
A.showValue1()
A.sum(2,3)
A.sum2(2,3)