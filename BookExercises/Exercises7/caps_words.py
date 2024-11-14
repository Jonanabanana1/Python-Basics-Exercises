# Write a function that takes a string as an argument and returns an all-caps version of the string when the string is longer than 10 characters. Otherwise, it should return the original string. Example: change 'hello world' to 'HELLO WORLD', but don't change 'goodbye'.
def caps_long_sentences(sentence):
    if len(sentence) > 10:
        return sentence.upper()
    else:
        return sentence
    
sentences = input('Enter text:\n')
print(caps_long_sentences(sentences))