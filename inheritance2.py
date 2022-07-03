class Person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("Myname is {}".format(self.name))
        print("Myidnumber is {}".format(self.idnumber))

# child class Person


class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        Person.__init__(self, name, idnumber)

    def details(self):
        print("Myname is {}".format(self.name))
        print("Myidnumber is {}".format(self.idnumber))
        print("Mypost is {}".format(self.post))


# creation of an object of the class person uing its instance
a = Employee('Rahul', 886012, 200000, "intern")
b = Person("Rohit", 99990)
b.details()
b.display()
a.display()
a.details()
