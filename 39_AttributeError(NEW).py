# Question: The script is supposed to output the cosine of angle 1 radian, but instead, it is throwing an error. Please fix the code so that it prints out the expected output.

# import math
# print(math.cosine(1))

# Expected output:
# 0.5403023058681397  

# Explanation
# we just need to check what inside math module is cosine present or not
import math
print(dir(math))
# then we got to know wxact word is cos not cosine
print(math.cos(1))
