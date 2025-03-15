import string

letters = []
for letter in string.ascii_lowercase:
    with open(letter + ".txt", "r") as file:
        content = file.read()
        if content in "python":
            letters.append(content)
print(letters)
