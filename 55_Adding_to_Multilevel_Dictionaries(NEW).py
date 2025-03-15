# Please add a new employee to the dictionary.

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
# Answer: 
d["employees"].append(dict(firstName = "Albert", lastName = "Bert"))

# Explanation:
# d['employees']  returns this list:

# [{"firstName": "John", "lastName": "Doe"},
#  {"firstName": "Anna", "lastName": "Smith"},
#  {"firstName": "Peter", "lastName": "Jones"}]
# Then d["employees"].append(dict(firstName = "Albert", lastName = "Bert"))  appends a new item to the list. This item happens to be a new dictionary.
