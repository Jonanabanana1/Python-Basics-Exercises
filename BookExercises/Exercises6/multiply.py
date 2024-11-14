# Write a program that uses a multiply function to multiply two numbers and returns the result. Ask the user to enter the two numbers, then output the numbers and result as a simple equation.
def multiply(a, b):
    return a * b
number_one = float(input('Enter the first number'))
number_two = float(input('Enter the second number'))
print(f'{number_one} * {number_two} = {multiply(number_one, number_two)}')