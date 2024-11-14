# Print all of the even numbers in the following list of nested lists. Don't use any while loops.
# my_list = [
#     [1, 3, 6, 11],
#     [4, 2, 4],
#     [9, 17, 16, 0],
# ]
# for sets in my_list:
#     for number in sets:
#         if number % 2 == 0:
#             print(number)

# write code that creates a new list with one element for each number in my_list. If the original number is an even, then the corresponding element in the new list should contain the string 'even'; otherwise, the element should contain 'odd'.
my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]
parity_list = []
for number in my_list:
    if number % 2 == 0:
        parity_list.append('Even')
    else:
        parity_list.append('Odd')
print(parity_list)