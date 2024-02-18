# the try block is used to test a block of code for errors to catch exceptions with the except block and then handle them with the finally block (if needed).
# the except block is used to catch exceptions with the try block and then handle them with the finally block (if needed). 
# the finally block is used to execute code, regardless of the result of the try- and except blocks. 
# the else block is used to execute code if the try block does not raise an exception.
# the raise block is used to raise an exception.
# the assert block is used to check if a condition is True, if not, the program will raise an AssertionError.



try:
    value=10/0
    number = int(input(" enter a number : "))
    print(number)

except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")
    


