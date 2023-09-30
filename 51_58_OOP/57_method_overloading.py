class Area:
    def find_area(self,x=None,y=None):
        if x!=None and y!=None:
            print(x*y)
        elif x!=None:
            print(x*x)
        else:
            print("Nothing")

a=Area()
a.find_area()
a.find_area(4)
a.find_area(4,5)