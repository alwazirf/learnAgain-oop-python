class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"

# creating a derived class


class Derived(Base):
    def __init__(self):
        # calling constructor
        Base.__init__(self)
        print("calling private member of base class")
        print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)
