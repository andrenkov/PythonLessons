myarray = [0, 3.62, 5.25, 11]
for n in myarray:
    print(n)
print("1-----------------")

# string as an array
mystr = "python test"
for s in mystr:
    print(s)
print("2-----------------")

for s in mystr:
    if s == " ":
        break
else:  # else works if there is no break in loop
    print("mystr", s)
print("3-----------------")

# array generators

# range is a generator of numbers from 2 to 15
myarray = list(range(2, 15))
print(myarray)
for n in myarray:
    print(n)
print("3-----------------")

# make list using the range() functions
myarray = [i for i in range(1, 10)]
print(myarray)

# print even numbers only
myarray = [i for i in range(1, 10) if i % 2 == 0]
print(myarray)
print("4-----------------")
