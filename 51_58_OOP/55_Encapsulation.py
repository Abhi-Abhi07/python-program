class Student:
    # strating me __ lagane se variable or method private ban jate he
    __name="Abhi"
    def __init__(self):
        print(self.__name)
        self.__display()

    def __display(self):
        print("Jay Shree Ram")

obj=Student()

