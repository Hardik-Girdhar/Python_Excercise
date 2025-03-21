# Question: Please complete the code so that it prints out the expected output.

a = [1, 2, 3] 

# Expected output: 
# Item 1 has index 0
# Item 2 has index 1
# Item 3 has index 2

# Answer:
a = [1, 2, 3]
for index, item in enumerate(a):
    print(f"Item {item} has index {index}")
  
# Explanation:
# enumerate(a)  creates an enumerate object which yields pairs of indexes and items. Then we iterate through that object print out the 
# item-index pairs in each iteration together with some other strings.

for i in range (len(a)):
    print(f"Item {a[i]} has index {i}")
