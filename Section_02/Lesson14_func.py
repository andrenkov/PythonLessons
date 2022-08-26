#func declaration
def printPython():
    print("Python")
# call func
printPython()

def sum(x, y):
    return x + y
# call func
s = sum(3, 89)
print(s)

def sumprint(x, y, r=False):
    if r:
        return r
    else:
        print(x + y)
# call func
sumprint(36, 4)
sumprint(36, 4, True)

#calling with param name
sumprint(x = 36, y = 4)
sumprint(y = 36, x = 4)

# any number of params
# workng like tuple
def bigsum(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s
print(bigsum(3, 5,7,7,3,2,909))

# passing a dictionary
def printdict(**dict):
    for key in dict:
        print(key, "=",dict[key])
printdict(name="vlad", age=33)

#anonimous func
lambdafunc = lambda x, y : print (x + y)
# call it
lambdafunc(3, 18)

# or
result = (lambda x, y: x + y)(4, 9)
print(result)

print("--- exercise ---")
def maxNum(arr):
    mymax = arr[0];
    for n in arr:
        if n > mymax:
            mymax = n
    return mymax

print(maxNum([3, 7, 5, 8, 90, -22]))





