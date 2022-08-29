from math import sqrt

class MyPoint:
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def range(self, p):
        return sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)

    # overrides the default str func
    def __str__(self):
        return "Coordinates : (" + str(self.x) + str(self.y) + ")"


class AutoMob:
    p = MyPoint(0, 0)
    speed = 0

    def __init__(self, p=MyPoint(0, 0), speed=40):
        self.p = p
        self.speed = speed

    def setSpeed(self, speed):
        self.speed = speed

    def getTime(self, endp):
        if self.speed != 0:
            return self.p.range(endp) / self.speed
        else:
            return 0


p = MyPoint(5, 10)
print(p)
print(p.range((MyPoint())))

auto = AutoMob()
auto.setSpeed(60)
print(auto.speed)
print(auto.getTime(MyPoint(100, 200)))
auto.setSpeed(0)
print(auto.getTime(MyPoint(100, 200)))
auto.setSpeed(30)
print(auto.getTime(MyPoint(100, 200)))
