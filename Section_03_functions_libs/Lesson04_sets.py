set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(len(set1))

# add element. order will not be consistent though
set1.add(3.62)
print(set1)
# delete element
set1.remove(3.62)
print(set1)
# delete if found
set1.discard(999)  # element not exist
print("------------------------")

# working with sets (intersections, comparing sets etc.)
print(set1 == set2)  # False
print(set1 <= set2)  # True set1 included into set2. Is subset
print(set1 >= set2)  # False set2 included into set1
# or use func issubset
print(set1.issubset(set2))  # True
print("------------------------")

# union
set1 = {2, 3, 4}
set2 = {1, 2, 3}
print(set1.union(set2))  # {1, 2, 3, 4}
# intersection
print(set1.intersection(set2))  # {2, 3}
# difference
print(set1.difference(set2))  # {4}
# clear
set1.clear()
print(set1)





