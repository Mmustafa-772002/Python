# the function is basically collection of code that can be called whenever needed that perform a tasks in the program.
# def is used to write a function in python 
# the indent is main part of python program that cause by the spaces or alignment of code in the program.
# to write the funtion name in the there are rules to write the function name
# 1. the name of the function should be in lowercase
# 2. the name of the function should be in camel case
# 3. the name of the function should be in snake case
# 4. the name of the function should be in pascal case
# 5. the name of the function should be in kebab case
# 6. the name of the function should be in upper case
# 7. the name of the function should be in title case
# 8. the name of the function should be in constant case
def say_hi(): 
    print("Hello User")
# to print the output we have to call the function in the program
say_hi()
# or we can also print the output by using the print function
print(say_hi())

# This is a function that will print Hello User
#  a parameter is a piece of information that is defilned in the function
#  name is parameter in the function say_hi 
def hello(name , age ):
    print("Hello " + name + " your are age is " + str(age))

hello("ali",50)
hello("khan",20)
