# In Python, fields can be created dynamically inside the constructor, but it's better to add it to the class design.
class MyCircle:
    x = 0
    y = 0
    r = 0

    def __init__(self, x, y, r=0):  # def __init__(self):  # built-in constructor
        self.x = x
        self.y = y
        self.r = r
        if r == 0:
            print("No radius!")


c = MyCircle(3, 4, 5)
print(c.x, ';', c.y, ';', c.r)
# new object
c = MyCircle(6, 7)
print(c.x, ';', c.y, ';', c.r)
