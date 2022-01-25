# some_list[START:STOP:STEP]
list_for_slice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
new_list = list_for_slice[0::2]

print(new_list)
print(list_for_slice)

first_three = slice(3)
list_slice_two_step = slice(None , None, 2)

print(list_for_slice[first_three])
print(list_for_slice)
print(list_for_slice[list_slice_two_step])