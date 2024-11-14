# Write Python code to print the seventh number of range(0, 25, 3).
# numbers = list(range(0, 25, 3))
# print(numbers[6])

# Use slicing to write Python code to print a 6-character substring of 'Launch School' that begins with the first c.
# school = 'Launch School'
# first_c_index = school.find('c')
# print(school[first_c_index:first_c_index+6])

#Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple should be in reverse order from the original. It should also exclude the first and last members of the original. The result should be the tuple (4, 3, 2).
# my_tuple = (1, 2, 3, 4, 5)
# reversed_tuple = tuple(reversed(my_tuple[1:len(my_tuple)-1]))
# print(my_tuple)
# print(reversed_tuple)


# Part 1: Write some code to print Bark by accessing the element associated with the key Dog.
# Part 2: Write some code to print None when you try to print the value associated with the non-existent key, Lizard.
# Part 3: Write some code to print <silence> when you try to print the value associated with the non-existent key, Lizard.

# pets = {
#     'Cat':  'Meow',
#     'Dog':  'Bark',
#     'Bird': 'Tweet',
# }

# print(pets['Dog'])
# print(pets.get('Lizard'))
# print(pets.get('Lizard', '<silence>'))

# Write Python code to replace all the : characters in the string below with +.
# info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
# print(f'Old text: {info}')
# new_info = info.replace(':', '+')
# print(f'New text: {new_info}')

# Write some code to replace the value 6 in the following nested list with 606:
# stuff = [
#     ['hello', 'world'],
#     ['example', 'mem', None, 6, 88],
#     [4, 8, 12],
# ]
# You don't have to search the list. Just write an assignment that replaces the 6
# print(stuff)
# stuff[1][3] = 606
# print(stuff)

# Write one line of code to print the activities that Cocoa enjoys.
# cats = {
#     'Pete': {
#         'Cheddar': {
#             'color': 'orange',
#             'enjoys': {
#                 'sleeping',
#                 'snuggling',
#                 'meowing',
#                 'eating',
#                 'birdwatching',
#             },
#         },
#         'Cocoa': {
#             'color': 'black',
#             'enjoys': {
#                 'eating',
#                 'sleeping',
#                 'playing',
#                 'chewing',
#             },
#         },
#     },
# }
# print(cats['Pete']['Cocoa']['enjoys'])

# Write some code that determines and prints whether the number 3 appears inside each of these lists:
# numbers1 = [1, 3, 5, 7, 9, 11]
# numbers2 = []
# numbers3 = [2, 4, 6, 8]
# numbers4 = ['1', '3', '5']
# numbers5 = ['1', 3.0, '5']
# This is the stupid way
# print(True) if (numbers1.count(3) > 0) else print(False)
# print(True) if (numbers2.count(3) > 0) else print(False)
# print(True) if (numbers3.count(3) > 0) else print(False)
# print(True) if (numbers4.count(3) > 0) else print(False)
# print(True) if (numbers5.count(3) > 0) else print(False)
# Dont know why i didnt think about this
# print(3 in numbers1)

my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

print(list(zip(my_str, my_list, my_tuple, my_range)))