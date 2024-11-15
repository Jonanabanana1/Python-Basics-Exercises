# region Old
# def multiply(left, right):
#     return left * right
# def bruce_eckel_quote():
#     print('Python is executable pseudocode')
# def cite(author, quote):
#     print(f'{author} said: "{quote}"')

# cite('Bruce Eckel', 'Python is executable pseudocode.')
# Bruce Eckel said: "Python is executable pseudocode."
# def squared_number(number):
#     return number * number

# # Write a function that compares the length of two strings. It should return -1 if the first string is shorter, 1 if the second string is shorter, and 0 if they're of equal length. For example:
# def compare_by_length(first, second):
#     firstlen = len(first)
#     secondlen = len(second)
#     if firstlen < secondlen:
#         return -1
#     elif secondlen < firstlen:
#         return 1
#     else:
#         return 0
    


# Use Python's string methods on the string 'Captain Ruby' to create a string with the value 'Captain Python'.
# ruby = 'Captain Ruby'
# python = ruby.replace('Ruby', 'Python')
# print(python)
# endregion

def greet(language_code):
    match language_code:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return "Haai!"
        case _:
            return 'error'
    
def greet_locally(region):
    match region:
        case 'US':
            return 'Hey!'
        case 'GB':
            return 'Hello!'
        case 'AU':
            return 'Howdy!'
        case _:
            return 'Hey!'
        
def extract_language(code):
    language = code[0:2]
    return language
def extract_region(code):
    region = code[3:5]
    return region

def local_greet(code):
    language = extract_language(code)
    region = extract_region(code)
    if language != 'en':
        return greet(language)
    return greet_locally(region)

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!
print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!

