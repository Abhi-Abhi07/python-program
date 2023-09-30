class A:
    b=30
    def getA(self):
        return self.a

    def setA(self,value):
        self.a=value

    def __init__(self):
        self.name=""
    def getname(self):
        return self.name
    def setname(self,name):
        self.name=name

obja=A()
obja.setA(10)
print(obja.getA())
obja.setname("Abhi")
print(obja.getname())
