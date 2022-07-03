class Base(object):
    def __init__(self, x):
        self.x = x


class Derivered():
    def __init__(self, x, y):
        Base.x = x
        self.y = y

    def printXY(self):
        print(Base.x, self.y)


d = Derivered(20, 30)
d.printXY()
