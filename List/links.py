a = "Word"
b = a
print(id(a))
print(id(b))
print(a is b) #check equivalence id

if a is b:
    print("Ok")

x = "Hello"
print(id(x))
x += " World"
print(id(x))



