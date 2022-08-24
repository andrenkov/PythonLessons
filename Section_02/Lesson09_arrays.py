list = []
print(list)
list = [1, 4, 6]
print(list)
list = ['h', 'e', 'l', 'l', 'o']
print(list)
print(list[1])
# get element from the END use minus
print("Last element", list[-1])
print("Last element", list[-2])

print("Length : ", len(list))
print("Last element", list[len(list) - 1])
print("----------------")

i = 0
while i < len(list):
    print(list[i])
    i += 1
print("----------------")

i = 0
list = ['z', 'x', 'v', True, 3.62]
while i < len(list):
    print(list[i])
    i += 1
print("----------------")

# multidimensional arrays
list = [[3, 4], [5, 6, 7], [8, 9]]
i = 0
while i < len(list):
    j = 0
    while j < len(list[i]):
        print(list[i][j])
        j += 1
    i += 1
print("----------------")

# find max and min element
prices = [20, 45, 30, 15]
min = prices[0]
max = prices[0]
i = 1
while i < len(prices):
    if prices[i] < min:
        min = prices[i]
    if prices[i] > max:
        max = prices[i]

    i += 1
print("min =", min)
print("max =", max)
print("----------------")

