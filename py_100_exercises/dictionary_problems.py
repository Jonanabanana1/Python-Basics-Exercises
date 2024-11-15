# car = {
#     'type'   : 'sedan',
#     'color'  : 'blue',
#     'mileage': 80000,
# }
# car['year'] = 2003
# del car['mileage']

# print(car)
# print(car['color'])
# print(len(car))


# Check whether the keys 'name' and 'grade' exist in the following dictionary:
# student = {
#     'id': 123,
#     'grade': 'B',
# }
# print(student.get('name'))
# print(student.get('grade'))

# vehicle = {
#     'car': {
#         'type' : 'sedan',
#         'color': 'blue',
#         'year' : '2003',
#     },
#     'truck': {
#         'type' : 'pickup',
#         'color': 'red',
#         'year' : '1998',
#     }
# }

# car = [
#     ['type', 'sedan'],
#     ['color', 'blue'],
#     ['year', 2003],
# ]

# Use a for loop to iterate over the numbers dictionary and return a list containing each number divided by 2 as an integer. The result should be truncated to an integer. Assign the returned list to a variable named half_numbers and print its value using print.
numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}
# half_numbers = []
# for number in numbers.values():
#     half_numbers.append(number // 2)
# print(half_numbers)
for pair in numbers:
    print(f'A {pair} number is {numbers[pair]}.') # Dumb way

for key, value in numbers.items():
    print(f'A {key} number is {value}.')
