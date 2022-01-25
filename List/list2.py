list_1 = [0] * 3
print(list_1)
list_1[0], list_1[1] = 3, 4
list_1[-1] = 2
print(list_1)

list_1.pop()
print(list_1) # whithout argument pop() delite last element
list_1.pop(1)
print(list_1)

list_1.insert(0, 1)
print(list_1)

list_2 = [1, 3, 7, 2, 10, 8]
list_2.sort()
print(list_2)
list_2.reverse()
print(list_2)
