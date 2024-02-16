# to building a basic calculator in python
# we have to take the input from the user
# then we have to perform the operation on the input
# then we have to print the output of the operation

num1 = float(input("Enter a number: "))
op = input("Enter the operator: ")
num2 = float(input("Enter a number: "))
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op =="/":
    result = num1 / num2
else:
    result = "Invalid operator"
    
print("The result is: " + str(result))
