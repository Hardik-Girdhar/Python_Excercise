# Question: Calculate the sum of the values of keys a  and b .

d = {"a": 1, "b": 2, "c": 3}

# Expected output: 
# 3

print(d["b"] + d["a"])

sum = 0
for value in d.values():
    sum = sum + value
print(sum)
