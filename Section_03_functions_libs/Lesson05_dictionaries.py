d = {'name':'Vlad', 'age':57}
print(d)

# add new element
d.setdefault('IsEmployed', True)
print(d)  # {'name': 'Vlad', 'age': 57, 'IsEmployed': True}
# get value by key
print(d.get('age'))  # 57
# remove element
d.pop('IsEmployed')
print(d)  # {'name': 'Vlad', 'age': 57}
# get all keys
print(d.keys())  # dict_keys(['name', 'age'])
# convert dict_keys above into an array
print(list(d.keys()))  # ['name', 'age']
# get values
values = list(d.values())
print(values)  # ['Vlad', 57]
print(values[1])  # 57
# update value
d['age'] = 58
d['gender'] = 'Male'  # this inserts new key-value automatically
print(d)

d.clear()
