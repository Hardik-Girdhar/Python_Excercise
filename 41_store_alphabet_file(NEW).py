# Create a script that generates a text file with all English letters inside it, one letter per line.
 

import string
 
with open("letters.txt", "w") as file:
    for letter in string.ascii_lowercase:
        file.write(letter + "\n")

with open("letters.txt", "r") as file:
    content = file.read()
print(content)
# Explanation:
# The ascii_lowercase   property of the string  module is quite helpful here to generate a string of all letters. 
# Then we create a file, and while the file is open, we iterate through the string and apply the write method in each
# iteration to write the letters in the text file. We are also appending \n  to each letter, which is a special character 
# that creates break lines. That makes sure to separate the letters in different lines.
