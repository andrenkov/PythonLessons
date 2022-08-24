import random

print("Enter number of elements:")
a = int(input())

arr = [int(random.random() * 10) for i in range(0, a)]
print(arr)
x = 0
while x < a:
    print(arr[x])
    x += 1

# remove duplicates
mylist = set(arr)
print(list(mylist))

for s in mylist:
    print(s)


