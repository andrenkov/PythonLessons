b1 = True
b2 = False
print("b1 =", b1)
print("b2 =", b2)

print("b1 or b2", b1 or b2)
print("b1 and b2", b1 and b2)
print("not b1", not b1)
print("b1 != b2", b1 != b2)
print("b1 == b2", b1 == b2)

x = 5
# casting into bool, it's False if integer = 0 and is True for any other int value
print("x and b1 or (x > 10) =", x and b1 or (x > 10))
