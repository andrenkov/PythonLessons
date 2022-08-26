s1 = "string 1"
s2 = "string 2"
print(len(s1))
print(s1[1])  # "t"
print(s1[-1])  # "1" from the end
print(s1[1:4])  # substring 1-3 "tri"

s1 = "abd\nzxc"
s2 = r"abd\nzxc"  # r is for screening ALL special symbols
print(s1)
print(s2)  # "abd\nzxc"
s1 = "abd\\nzxc" # r is for screening next symbol
print(s1)
print("-----------------")
s1 = "hello"
print(s1 * 2)  # hellohello

print(s1.find("l"))  # 2 - first occurrence
print(s1.find("l", 3))  # 3 - first occurrence after 3 position
print(s1.find("l", 4))  # -1 - first occurrence after 4 position

print(s1.isdigit())  # bool numbers only
print("123".isdigit())  # true
print("12.3".isdigit())  # false
print("12.3".isdecimal())  # false
print("123".isdigit())  # true
print(s1.isalpha())  # bool - letters only

print(s1.upper())
print(s1.lower())

print("-----------------")
print(ord("a"))  # 97
print(chr(97))  # "a"

s1 = "  hello dear    "
print(s1.strip())  # "hello dear"

# Formatting string
s1 = "Hello, {0}. You are {1} years old"
print(s1.format("Vlad", "57"))

s1 = "Hello, {name}. You are {age} years old"
print(s1.format(name='Vlad', age='57'))

# format with tuples
data = ('Vlad', 57)
s1 = "Hello, {0[0]}. You are {0[1]} years old!"
print(s1.format(data))

# formatting numbers
s1 = "int: {0:d}; bin: {0:b}; float: {0:f} "
print(s1.format(5))  # int: 5; bin: 101; float: 5.000000

# rounding
s1 = "Round (150 / 47): {0:.3}"  # show 3 numbers only
print(s1.format(150 / 47))  # Round (150 / 47): 3.19
print(s1.format(1500 / 47))  # Round (150 / 47): 31.9

