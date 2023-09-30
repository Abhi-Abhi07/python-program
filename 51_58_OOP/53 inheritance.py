class A:
    a=10

    def displayA(self):
        print("Class is A")

class B(A):
    b=20

    def displayB(self):
        print("class is B")
# # class ke name se data ko access kar rhe hai
# print(B.a)
# print(B.b)

objb=B()

print(objb.a)
print(objb.b)
objb.displayA()
objb.displayB()

print()
print(objb.a)
objb.displayA()
print(B.a) # class ke name se data ko access kar rhe hai
# B.displayA() # show error because class ke name se method ko access nhi kar sakte hai

