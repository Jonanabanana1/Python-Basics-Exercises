# Write a function that computes and returns the factorial of a number by using a for or while loop. 
# start loop starting at 1 and ending at number+1
# I keep track of sum and just do sum*=index
def factorial(number):
    product = 1
    for factor in range(1, number+1):
        product *= factor
    return product
print(factorial(3))
print(factorial(4))