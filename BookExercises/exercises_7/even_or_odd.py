# Write a function, even_or_odd, that determines whether its argument is an even or odd number. If it's even, the function should print 'even'; otherwise, it should print 'odd'. Assume the argument is always an integer.
def even_or_odd(num):
    # if (num % 2) == 0:
    #     print('even')
    # else:
    #     print('odd')
    print('even' if num % 2 == 0 else 'odd')

even_or_odd(4)
even_or_odd(5)