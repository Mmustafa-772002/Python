# exponent function - a function that takes two numbers as parameters and returns the first number raised to the power of the second number
 
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range (pow_num):
        result = result * base_num
    return result

print(raise_to_power(2,3))

# Output:
# 8
#
# In the above example, the function raise_to_power takes two parameters base_num and pow_num.
# The function returns the first number raised to the power of the second number.
# The for loop is used to calculate the result.


