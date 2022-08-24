# tuples are read only lists (list of const)
# takes less RAM if you comparer it with List
mytuple = tuple()
print(mytuple)

# tuple with one element must have a comma
mytuple = (1,)
print(mytuple)

mytuple = (0, '4','6', 3.62)
print(mytuple)

mytuple = tuple("Pythonnn")
print(mytuple)
# error
# mytuple[3] = "T"
print(mytuple)

mytuple = tuple("Python")
for s in mytuple:
    print(s)

