class A:
    a=10
    def displayA(self):
        print("A")

class B:
    b=20
    def displayB(self):
        print("b")

class C(A,B):
    c=30
    def displayC(self):
        print(C)
        print("C")

objc=C()
print(objc.b)
objc.displayA()
objc.displayC()
