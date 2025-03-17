# Answer: 

import json
from pprint import pprint
 
with open("company1.json","r") as file:
    d = json.load(file.read())
 
pprint(d)

# Explanation:
# We're opening the file in read mode and then using json.load  which gets a string as output and creates a dictionary object out of that.

