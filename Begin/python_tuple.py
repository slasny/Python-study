import numbers
from unicodedata import name


not_a_tuple = (100) #it is not a tuple
print(type(not_a_tuple))
it_is_tuple = (100,)
print(type(it_is_tuple))

numbers = (1,2,3,4,5)
for i in numbers:
    print(i)

def return_tuple(a,b,c,d):
    sum = a + b
    multi = a * c
    divide = d / a
    return (sum, multi, divide)

it_tuple_return_from_method = return_tuple(12, 23, 4, 5)
print(it_tuple_return_from_method)

name_and_age = ("Obama", 100)
(name, age) = name_and_age

print(age)
print(name)