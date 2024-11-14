# Write a program named age.py that asks the user to enter their age, then calculates and reports the future age 10, 20, 30, and 40 years from now. Here's the output for someone who is 27 years old.

age = input('What is your age?\n')
print(f'You are {age} years old')
for i in range(1,5):
    print(f'In {i*10} years, you will be {int(age) + (i*10)} years old.')