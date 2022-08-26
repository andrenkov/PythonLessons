# in dictionaries, there's no a key by a sequential index. Index could be a number, a string etc. key-value pairs

mydict = dict();
# print(mydict)
# or
mydict = {'Name' : 'Vlad', 'Age' : '57'}
print(mydict)

# or
mydict = dict(Name='Vlad', Age=57, IsMale=True)
print(mydict)

# Search value by Key
age = mydict["Age"]
print(age)

print("----------------------")
for key in mydict:
    print(key, "=", mydict[key])

print("----------------------")
# using tuple
mytuple = ('Name','Age','IsMale')
for key in mytuple:
    print(key, "=", mydict[key])

print("----------------------")
#generating dictionary example
mydict = {str(i * 2) : i for i in range(1, 10)}
print(mydict)

print("---  Exercise ---")

myuser = mydict = dict(Name='NA', Age=-1)
print("Enter your name:")
name = input()
print("Enter your age:")
age = input()

myuser['Name'] = name
myuser['Age'] = age
print(myuser)