# abstract is a class from which you cannot create an object, but only create child classes
# require the abs namespace to be imported
from abc import ABC, abstractmethod


# ABC is an abstract class attribute  !!!!!!!!!!!!!!!!!!!!!!!!
class Shape(ABC):
    x = 0
    y = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def PrintXY(self):
        print('(X Y :', str(self.x), ';', str(self.y), ')')

    # abstract method. Must be implemented in child classes  !!!!!!!!!!!!!!!!!!!!!!!
    @abstractmethod
    def draw(self):
        pass  # pass null operation (void) used here to avoid syntax error when there's code in the method


class MyCircle(Shape):  # child class of Shape
    r = 0

    def __init__(self, x, y, r):
        Shape.__init__(self, x, y)
        self.r = r

    def draw(self):
        print('Drawing circle:', str(self.r))


class MyRect(Shape):  # child class of Shape
    w = 0
    h = 0

    def __init__(self, x, y, w, h):
        Shape.__init__(self, x, y)
        self.w = w
        self.h = h

    def draw(self):
        print('Drawing rect:', str(self.w), str(self.h))


# Shape is an abstract class
# s = Shape(6,78)
# s.PrintXY()
# s.draw()

c = MyCircle(30, 40, 20)
c.draw()

r = MyRect(50, 30, 10, 15)
r.draw()
