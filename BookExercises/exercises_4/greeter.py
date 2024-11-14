# Write a program named greeter.py that greets 'Victor' three times. Your program should use a variable and not hard code the string value 'Victor' in each greeting.
name = 'Victor'
for i in range(0, 3):
    time = ''
    if i == 0:
        time = 'Morning'
    elif i == 1:
        time = 'Afternoon'
    else:
        time = 'Evening'
    print(f'Good {time}, {name}.')