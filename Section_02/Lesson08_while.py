i = 0
while i < 5:  # lines blocks after ":" must be with Indent
    print("i =", i)
    i += 1
print("while has been perfomed")
print("___________________")

i = 0
while i < 5:  # lines blocks after ":" must be with Indent
    i += 1
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
print("___________________")

s = 0
x = 1
to = 10
while x <= to:
    s += x
    x += 1
print("Summary from 1 to", to, " = ", s)

while True:
    code = input("Enter Zero to exit :")
    if code == "0":
        break

exit(0) # close the program
