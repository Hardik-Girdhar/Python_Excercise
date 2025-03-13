# Question: Filter the dictionary by removing all items with a value of greater than 1.

d = {"a": 1, "b": 2, "c": 3}

# Expected output: 
# {'a': 1}  

ans = {}
for key,value in d.items():
    if(value <= 1):
        ans[key] = value
print(ans)

# --------------------

to_dlt = []
for key,value in d.items():
    if(value > 1):
        to_dlt.append(key)
      
for key in to_dlt:
    del d[key]
print(d)
