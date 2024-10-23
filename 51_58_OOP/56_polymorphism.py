# l=[10,20,30,40]
# print(len(l))
#
# s="Radhe Radhe"
# print(len(s))

class Ai:
    def displayinfo(self,name=''):
        print("Welcome "+name)

    def info(self):
        print("I am Ai")

class Ak(Ai):
    def info(self):
        super().info()
        print("I am Ak")

obj=Ai()
# overloadding
obj.displayinfo()
obj.displayinfo("Abhi")

# overriding
obj2=Ak()
obj2.info()