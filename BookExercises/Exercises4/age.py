#Write a program named age.py that includes someone's age and then calculates and reports the future age 10, 20, 30, and 40 years from now. Here's the output for someone who is 22 years old.
age = 22
future_age = age
print(f'You are {age} years old.')
for i in range(1, 5):
    future_age = age + (i*10)
    print(f'In {i*10} years, you will be {future_age} years old.')