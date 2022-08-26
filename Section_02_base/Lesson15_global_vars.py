def sum(x, y):
    s = float(x) + float(y)
    global result # this forces to use the global "result" instead of making new local var "result"
    result = s
    return s

x = input("Enter nvalue for x: ")
y = input("Enter nvalue for y: ")
print("Sum = ", sum(x, y))

result = 0
sum(x, y)
print(result)
