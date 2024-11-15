# Write a function that returns the first element of a list provided as an argument.
# def first(list):
#     if not list:
#         return None
#     return list[0]

# print(first(['Earth', 'Moon', 'Mars']))  # Earth


# Write a function that returns the last element of a list provided as an argument. 
# def last(list):
#     if not list:
#         return None
#     return list[-1]

# print(last(['Earth', 'Moon', 'Mars']))  # Mars


# Write some code to remove 'fossil' from the list, then add 'geothermal' to the end of the list.
# energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']
# energy.remove('fossil')
# energy.append('geothermal')
# print(energy)


# Split the string alphabet into a list of characters.
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# alphabet_list = list(alphabet)
# print(alphabet_list)


# Count the number of elements in scores that are 100 or above.
# scores = [96, 47, 113, 89, 100, 102]
# count = 0
# for score in scores:
#     if score >= 100:
#         count += 1
# print(count)


# You've been given a list of vocabulary words grouped into sub-lists, by meaning. This is a two-dimensional list or a nested list. Write some code that iterates through and prints all the words, one per line.
# vocabulary = [
#     ['happy', 'cheerful', 'merry', 'glad'],
#     ['tired', 'sleepy', 'fatigued', 'drained'],
#     ['excited', 'eager', 'enthused', 'animated'],
# ]

# for group in vocabulary:
#     for emotion in group:
#         print(emotion)


# How can you check if a variable holds a value that is a list? Given two variables, verify whether the values they hold are lists.
# some_value1 = [0, 1, 0, 0, 1]
# some_value2 = 'I leave you my Kingdom, take good care of it.'
# print(type(some_value1) is list)
# print(type(some_value2) is list)


# Write a function that checks whether a destination is in the list without using 'in' operator
# destinations = ['Prague', 'London', 'Sydney', 'Belfast',
#                 'Rome', 'Aruba', 'Paris', 'Bora Bora',
#                 'Barcelona', 'Rio de Janeiro', 'Marrakesh',
#                 'New York City']

# def contains(key, items):
#     for item in items:
#         if item == key:
#             return True
#     return False

# print(contains('Barcelona', destinations)) # True
# print(contains('Nashville', destinations))  # False


# We generated parts of a passcode and now want to combine them into a string. Write some code that creates and prints a string that contains each portion of the passcode separated by hyphens (-).
# passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

# # Write some code here.
# joined_passcode = '-'.join(passcode)
# # Expected output: 11-jZ5-hQ3f*-8!7g3-p3Fs
# print(joined_passcode)


# Write code that removes the items from grocery_list, one by one, until it is empty. If you print the elements you remove, the expected behavior would look as follows.
grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

# Your code.

for _ in range(0, len(grocery_list)):
    print(grocery_list[0])
    grocery_list.pop(0)

print(grocery_list)