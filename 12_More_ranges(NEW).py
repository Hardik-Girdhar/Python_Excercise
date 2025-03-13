# Question: Complete the script so that it produces the expected output. Please use my_range  as input data.

my_range = range(1, 21)

# Expected output: 
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200] 

# we can do mutiplication of 10 with the output
print([10 * i for i in my_range])

# we can change the range also to get the same output
my_range = range(10, 210, 10)
print(list(my_range))
