# import random
# or we can import all and then we don't have to write random.randint(), but just randint()
from random import *

# import math
# or you can use aliases. Then we can use print(m.sin(0.5))
# import math as m
# or we can import only one or a few functions
from math import sin, cos

print(randint(1, 10))
# print(math.sin(0.5))
print(sin(0.5))

# to add custom module
import cals
print(cals.sum(3.62, 5.25))
