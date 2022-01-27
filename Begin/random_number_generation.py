from random import randint
from random import choice

random_number = randint(1, 100)
print(random_number)

string = "String"
random_index = randint(0, len(string) - 1)
char = string[random_index]
print(char)

string = "Another sample string"
char = choice(string)
print(char)
