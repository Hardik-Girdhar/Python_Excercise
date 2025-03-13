# Create a function that takes any string as input and returns the number of words for that string.

def word_count(string):
    string_list = list(string.split())
    return len(string_list)

print(word_count("Hello How are you"))
