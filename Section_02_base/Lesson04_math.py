x = 15
y = 20

print("x=", x)
print("y=", y)

# simple operations
print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)

#other operations
print("x % y =", x % y)  # =15 The modulo division operator produces the remainder of an integer division
x = 25
print("x % y =", x % y)  # =5 The modulo division operator produces the remainder of an integer division
# module used for odd and even numbers
# x = 5
x = 4
isOdd = x % 2 == 0
print("x is odd", isOdd)

# Floor of division
x = 55
print("x // y =", x // y)  # =2

# power of
x = 3
y = 2
#  3 power of 2
print("x ** y =", x ** y)  # =9

# bit operations
x = 5
y = 7
print("x =", bin(x))  # = 0b101
print("y =", bin(y))  # = 0b111

# hex (16)
print("x =", hex(x))  # = 0b101
print("y =", hex(y))  # = 0b111
x = 12
y = 25
print("x =", hex(x))  # = 0xc
print("y =", hex(y))  # = 0x19 (16 + 9)

# oct (8)
print("x =", oct(x))  # = 0o17
print("y =", oct(y))  # = 0o31
print("---------------------------------")

# binary OR
x = 5
y = 7
print("x =", bin(x))  # = 0b101
print("y =", bin(y))  # = 0b111
print("x | y =", x | y)
print("x | y =", bin(x | y))
# binary AND
print("x & y =", x & y)
print("x & y =", bin(x & y))
# binary XOR
print("x ^ y =", x ^ y)
print("x ^ y =", bin(x ^ y))
# binary Inversion
# binary One's Compliment operation
print("~x =", ~x)
print("~x =", bin(~x))
# Shifting
print("x << 1", x << 1)  # x * 2 = 10
print("x << 1", bin(x << 1))  # x * 2
print("x >> 1", x >> 1)  # x div 2 = 2
print("x >> 1", bin(x >> 1))
z = x >> 1
print("z =", z)