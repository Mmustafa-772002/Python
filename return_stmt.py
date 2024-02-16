# return stmt is used to return a value from the function. 
# The value can be of any type.
# The return statement is used to exit a function and go back to the place from where it was called    
def cube(num):
    num*num*num  # this will not return the value of the cube of the number
    
print(cube(3))

def cube(num):
    return num*num*num
    
print(cube(3))

def cube(num1):
    return num1*num1*num1

result=cube(4)
print(result)

user = int(input("Enter a number: "))
def square(user):
    return user*user

print(square(user))

