# Determine the length of the string "These aren't the droids you're looking for.".
# string = 'These aren\'t the droids you\'re looking for.'
# print(len(string))
# Convert the string 'confetti floating everywhere' to all upper case.
# string = 'confetti floating everywhere'
# print(string.upper())
# Using the following code, compare the value of name with the string 'RoGeR' while ignoring the case of both strings. Print true if the values are the same; print false if they aren't. Next, perform a case-insensitive comparison between the value of name and the string 'DAVE'.
# name = 'Roger'
# print(name == 'RoGeR')
# print(name.casefold() == 'RoGeR'.casefold())
# Write code that checks whether the string char_sequence contains the character x
# char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdxWsIG9mIGVlbHMu'
# has_x = 'x' in char_sequence
# print(has_x)
#Write a function that checks whether a string is empty or not.
# def is_empty(text):
#     return len(text) == 0
#     # return not text

# print(is_empty('mars'))  # False
# print(is_empty('  '))    # False
# print(is_empty(''))      # True
# Write an is_empty_or_blank function to determine whether a string is either empty or consists entirely of spaces. For example:
# def is_empty_or_blank(s):
#     stripped_string = s.strip()
#     return not stripped_string
# print(is_empty_or_blank('mars'))  # False
# print(is_empty_or_blank('  '))    # True
# print(is_empty_or_blank(''))      # True
# Write code that capitalizes the words in the string 'launch school tech & talk', so that you get the string 'Launch School Tech & Talk'.
# string = 'launch school tech & talk'
# cap_string = string.title()
# print(cap_string)
# Write a function that checks whether a string starts with a specific prefix.
# def starts_with(word, prefix):
#     return word.startswith(prefix)
# print(starts_with("launch", "la"))   # True
# print(starts_with("school", "sah"))  # False
# print(starts_with("school", "sch"))  # True
# Write a function that counts the number of occurrences of a substring in a string.
def count_substrings(word, substring):
    return word.count(substring)
print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0
