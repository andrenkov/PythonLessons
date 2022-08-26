print("Enter 0, 1 or 5:")
a = input()

# in if..else lines blocks after ":" must be with Indent (at least one space or tab) !!!!!!!!!!!!
if a == "0":
    print("You entered zero")
elif a == "1":
    print("You entered One")
    print("1 < 10")
elif a == "5":
    print("You entered Five")
    if int(a) == 5:
        print("Integer a =", a)
    else:
        print("Integer a <>", 5)
else:
    print("You entered number ", a)

cond = a == "0" or a == "1" or a == "5"
if cond:
    x = 0
else:
    x = 3

print ("x =", x)
# short version of the above
x = 0 if cond else 3
print ("x =", x)



