# Question: Complete the script so that it removes duplicate items from the list a .

a = ["1", 1, "1", 2]

# Expected output: 
#   ['1', 2, 1] 

b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)

print(set(a))
