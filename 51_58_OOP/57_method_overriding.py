class A:
    def showData(self):
        print("I am A")

class B(A):
    def showData(self):
        print("I am B")


obj=B()
obj.showData()