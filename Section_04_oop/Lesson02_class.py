# In Python, fields can be created dynamically, but it's better to add it to the class design.
class MyPoint:
    x = 0
    y = 0

# default constructor
p1 = MyPoint()
print(p1)  # <__main__.MyPoint object at 0x000001D18E9DAE90>
print(p1.x, ';', p1.y)
p1.x = 5
p1.y = 10
print(p1.x, ';', p1.y)

p2 = MyPoint()
p2.z = 10  # dynamic field added. p1 object still has no this z field
print(p2.x, ';', p2.y, ':', p2.z)
