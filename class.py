class Dog:
    attr1 = "mammal"

    def __init__(self, name):
        self.name = name


Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
print("Rodger is a {} ".format(Rodger.__class__.attr1))
print("Tommy is a {} ".format(Tommy.__class__.attr1))


# accessing instance attricutes
print("My name is {} ". format(Rodger.name))
print("My name is {} ". format(Tommy.name))
