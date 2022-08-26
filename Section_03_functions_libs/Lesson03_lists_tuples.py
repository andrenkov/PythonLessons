list = [0,2,5,48,2]
print(list)

# add into List
list.append(3.62)
print(list)
# add multiple items
list.extend([5.25, 65])
print(list)
# insert
list.insert(2, 333)  # insert into 2nd position/indx
print(list)  # [0, 2, 333, 5, 48, 2, 3.62, 5.25, 65]
print("------------------------")

print(list.index(333))  # index 2
print(list.index(5, 2)) # index of "5" starting search from position index 2
# count the number of occurrences
print(list.count(2))
# reverse the list
list.reverse()
print(list)
print("------------------------")

# delete item
list.remove(333)  # remove first occurrence of "333"
print(list)
# delete item by index
list.pop(5)
print(list)

# list.clear()
# print(list)

list.sort()
print(list)
list.sort(reverse=True)
print(list)

# tuples working the same way, but where data members are constants
t = tuple("Hello")
print(t.index("e"))
print(t.count("l"))
