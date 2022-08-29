# __ means Private
class MyPoint:
    __x = 0
    __y = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def getX(self):
        return self.__x;

    def getY(self):
        return self.__Y;

    def setX(self, x):
        self.__x = x;

    def setY(self, y):
        self.__Y = y;
    # private method
    def __TestPrivate(self):
        print('Private method')
    # public method
    def runTestPrivate(self):
        self.__TestPrivate()

p = MyPoint(10, 15)
print(p)
print(p.getX())
p.setX(25)
print(p.getX())

# p.__TestPrivate() error
p.runTestPrivate()

