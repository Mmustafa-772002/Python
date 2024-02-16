num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

def max_num(num1, num2, num3):
    if num1 <= num2 and num2 >= num3:
        print("The maximum number is " + str(num2))
        return num2
    elif num1 >= num2 and num1 >= num3:
        print("The maximum number is " + str(num1))
        return num1
    else:
        print("The maximum number is " + str(num3))
        return num3
    
print(max_num(num1,num2,num3))

# the compare operators are used to compare the values in the program 
# <, >, <=, >=, ==, != are the compare operators in the program 
# < `less than` is used to check the value is less than the other value in the program
# > `greater than` is used to check the value is greater than the other value in the program
# <= `less than or equal to` is used to check the value is less than or equal to the other value in the program
# >= `greater than or equal to` is used to check the value is greater than or equal to the other value in the program
# == `equal to` is used to check the value is equal to the other value in the program
# '!='  `not equal to` is used to check the value is not equal to the other value in the program


    