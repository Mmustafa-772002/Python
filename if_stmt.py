# the control statements in python are if, elif, else and nested if statements
# the if statement is used to check the condition in the program
# the elif statement is used to check the multiple conditions in the program
# the else statement is used to check the condition if the condition is not true
# the nested if statement is used to check the condition in the program
# the pass statement is used to do nothing in the program
# the break statement is used to stop the loop in the program
# the continue statement is used to skip the current iteration in the loop
# the return statement is used to return the value from the function
# the assert statement is used to check the condition in the program
# the raise statement is used to raise the exception in the program
# the import statement is used to import the module in the program
# the from statement is used to import the specific function from the module
# the as statement is used to rename the module in the program
# the global statement is used to declare the global variable in the program
# the nonlocal statement is used to declare the nonlocal variable in the program
# the del statement is used to delete the variable in the program
# the with statement is used to open the file in the program
# the try statement is used to handle the exception in the program
# the except statement is used to handle the exception in the program
# the finally statement is used to execute the code after try and except block
# the raise statement is used to raise the exception in the program
# the assert statement is used to check the condition in the program
# the yield statement is used to return the value from the function
# the lambda statement is used to create the anonymous function in the program
# the print statement is used to print the output in the program

from operator import is_


is_hungry = False
is_thirsty = True
if is_hungry or is_thirsty:
    print("you are hungry or thirsty")
    
else:
    print("you are not hungry")
    
    
if is_hungry and is_thirsty:
    print("you are hungry and thirsty")
    
else:
    print("you are not hungry and thirsty") 


    
if is_hungry:
    print("you are hungry")

elif is_hungry and not (is_thirsty):
    print("you are hungry and not thirsty")

elif is_thirsty and not (is_hungry):
    print("you are thirsty and not hungry")   
else:
    print("you are not hungry and thirsty")
