# # continue
#
# my_str = 'abcdef'
#
# for letter in my_str:
#     print('before continue')
#     if letter == 'd':
#         continue #this will stop current itteration
#     # if letter == 'f':
#     #     break #this will stop for loop
#     print(letter)
# else:
#     print('All is done')
#
# my_number = 0
#
# while my_number < 5:
#     print(my_number)
#     my_number += 1
# else:
#     print('all done')
#
#Lists
# my_var = 3.3
# my_list = ['a', 1, True, my_var]
#
# my_list.__iter__()
# my_list.append([])
# for obj in my_list:
#     print(obj)
#
# print(f'first object is: {my_list[0]}')
# print(f'second object is: {my_list[1]}')
# print(f'third object is: {my_list[2]}')
# print(f'fourth object is: {my_list[3]}')
# print(f'fifth object is: {my_list[-1]}')
#
# print(my_list.extend([1, 2, 3]))
#
# for obj in my_list:
#     print(obj)
#
# print(my_list)

#modifing objects

# a = "name: {}"
# print(f"Initial ID: {id(a)}")
# result = a.format('abcd')
# print("Identity of objects",id(a), id(result))
# print(a)
#
# b = ["name: {}"]
# print(f"Initial ID: {id(b)}")
# result = b.append('abcd')
# print("Identity of objects",id(b), id(result))
# print(b) #lists are mutable
#
# # mutable objects in modifing loops
#
# my_new_list = list('random')
#
# for letter in my_new_list:
#     my_new_list.pop()
#     print(letter)

for item in my_dict: