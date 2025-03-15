# in 45 we created letter file
# now we need to extract the content of the file and store in list
import string
letters = []
for letter in string.ascii.lowercase:
    with open(letter + ".txt" , "r") as file:
        letters.append(file.read())
print(letters)d
