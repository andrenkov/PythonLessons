import random
from typing import List

myset = set()  # use set function
print(myset)
myset = {}  # {} to create a SET
print(myset)

myset = set("pythonnnnn")
print(myset)

# only unique members will be present and duplicates will be ignored
myset = {0, 1, 2, 3, 2, 3, '0', '1'}
print(myset)

# set from array
mylist = [i for i in range(0, 10)]
print(mylist)
# convert to SET
myset = set(mylist)
print(myset)

# from 0 to 1
# print(random.random())
# generate random int list
arr = [int(random.random() * 10) for i in range(0, 10)]
print(arr)
myset = set(arr)  # to remove all duplicates. Very useful method
print(myset)
arr = list(set(arr))  # to remove all duplicates. Very useful method
print(arr)