# Question:  Why is there an error in the code, and how would you fix it?

# def foo(a=1, b=2):
#     return a + b

# x = foo - 1

def foo(a=1, b=2):
    return a + b

print(type(foo))   # it will be an function
print(type(foo())) # it will be an integer
# so we can change out output according to this

x = foo() - 1
