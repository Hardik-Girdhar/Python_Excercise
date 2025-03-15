# Question: Create a script that generates a file where all letters of the English alphabet are listed two in each line. The inside of the text file would look like:

# ab
# cd
# ef

# and so on.

import string
import string
with open("letter.txt" , "w"):
    for letter1, letter2 in zip(string.ascii_lowercase[0::2],string.ascii_lowercase[1::2]):
        print(letter1 + letter2 )

# ----------

import string
l1 = []
l2 = []
for i in string.ascii_lowercase:
    if( i == 'a'):
        l1.append(i)
    elif(i == 'z'):
        l2.append(i)
    else:
        l1.append(i)
        l2.append(i)
for i,j in zip(l1,l2):
    print(f"{i}{j}")
  
# -----------

for a1, a2 in zip(range(97,123) , range(98,123)):
    print(f"{chr(a1)}{chr(a2)}")
