# Write a function that takes a single integer argument and prints a message that describes whether:

    # the value is between 0 and 50 (inclusive)
    # the value is between 51 and 100 (inclusive)
    # the value is greater than 100
    # the value is less than 0

def int_size(value):
    if value < 0:
        print(f'{value} is less than 0')
    elif (value >= 0) and (value <= 50):
        print(f'{value} is between 0 and 50')
    elif (value >= 51) and (value <= 100):
        print(f'{value} is between 51 and 100')
    else:
        print(f'{value} is greater than 100')

number = int(input('Enter an integer:\n'))
int_size(number)