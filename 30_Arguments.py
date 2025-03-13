# Question:  Why do you get an error, and how would you fix it?

# def foo(a=2, b):
#     return a + b

def foo(b , a=2):
    return a + b

print(foo(2))

# we need to non default parameter in first so that they can take the value from function given by user
