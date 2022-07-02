class Car:

    def __init__(self):
        self.__lengthChassis = 250
        self.__wideChassis = 120
        self.__wheels = 4
        self.__isStart = False

    def start(self, start):
        self.__isStart = start
        if self.__isStart:
            checked = self.__inner_check()

        if self.__isStart and checked:
            return "The car has started"
        elif self.__isStart and checked==False:
            return "Something is bad, can't start"
        else:
            return "The car is stopped"

    def status(self):
        print("The car has", self.__wheels, "wheels.\nA length of ", self.__lengthChassis)

    def __inner_check(self):
        print("Doing inner check")

        self.gasoline = "ok"
        self.oil = "ok"
        self.doors = "ok"

        if self.gasoline == "ok" and self.oil == "ok" and self.doors == "ok":
            return True
        return False


myCar = Car()

print(myCar.start(True))
myCar.status()

print("----------Next we create the second object---------------------")

myCar2 = Car()
print(myCar2.start(False))
myCar2.status()
