class Myclass:

    __hiddenVariable = 0

    def add(self, increament):
        self.__hiddenVariable += increament
        print(self.__hiddenVariable)


myObject = Myclass()
myObject.add(2)
