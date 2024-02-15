from math import sqrt , floor
from math import *
# the above line is used to import the sqrt and floor functions from the math module
# this is the math module in that we are importing the sqrt and floor functions  from the math module 
# this module is used to perform the mathematical operations in python 
# working with numbers in python  :
# int data type : int data type is used to store the integer data in the variable
a = 5
print(a)

# output : 5

# float data type : float data type is used to store the float data in the variable
b = 5.5
print(b)

# output : 5.5

# negetive numbers in python  : the negetive numbers are also used in python
c = -5
print(c)

# output : -5

# addition of two numbers in python  : the addition of two numbers is done by using the plus operator
d = 5
e = 6
f = d + e
print(f)

# output : 11

# subtraction of two numbers in python  : the subtraction of two numbers is done by using the minus operator
g = 10
h = 5
i = g - h
print(i)

# output : 5
    
# multiplication of two numbers in python  : the multiplication of two numbers is done by using the star operator

j = 5
k = 6
l = j * k
print(l)
    
# output : 30

# division of two numbers in python  : the division of two numbers is done by using the slash operator
m = 10
n = 5
o = m / n
print(o)

# output : 2.0

# modulus of two numbers in python  : the modulus of two numbers is done by using the percentage operator

p = 10
q = 3
r = p % q
print(r)

# output : 1

# power of two numbers in python  : the power of two numbers is done by using the double star operator
s = 2
print(pow(s,2))
print(pow(s,3))

# to convert number into strings 
a =5
print(str(a))

# output : 5    

# the abs function is used to find the absolute value of the number
t = -5
print(abs(t)) 

#  output : 5

print(3*2+5)

# output : 11 

print(3*(2+5))

# output : 21

# the round function is used to round off the number
u = 5.5
print(round(u))

# output : 6

v = 25
print(sqrt(v))

# output : 5.0

# the max function is used to find the maximum number from the given numbers 
x = 20
y = 30
z = 40
print( " the max value is : " + str(max(x,y,z)))

# output : the max value is 40

# the min function is used to find the minimum number from the given numbers
a = 20
b = 30
c = 40
print( " the min value is " + str(min(a,b,c)))

# output : the min value is 20

# the sum function is used to find the sum of the given numbers
a = 20
b = 30

print("The sum value is: " + str(sum([a, b])))


# output : the sum value is 50

# the floor function is used to find the floor value of the given number
# floor number is the largest integer that is less than or equal to the number 
a = 5.5
print( " the floor value is " + str(floor(a)))

# output : the floor value is 5

# ceil is used to find the ceiling value of the given number 
# the ceiling number is the smallest integer that is greater than or equal to the number
a = 5.5
print( " the ceil value is " + str(ceil(a)))

# output : the ceil value is 6
# math function list in python 
# abs() : this function is used to find the absolute value of the number
# pow() : this function is used to find the power of the number
# sqrt() : this function is used to find the square root of the number
# max() : this function is used to find the maximum number from the given numbers
# min() : this function is used to find the minimum number from the given numbers
# sum() : this function is used to find the sum of the given numbers
# floor() : this function is used to find the floor value of the given number
# ceil() : this function is used to find the ceiling value of the given number
# round() : this function is used to round off the number
# the math module is used to perform the mathematical operations in python

# input in the python That makes the input that takes input from the user 
name = input("enter the name : ")
# varibale name = input (" string ")
print(" hello my name is " + name + " !!!")

# output : 
# enter the name : siva
# hello my name is siva !!!


age = input("enter the age : ")
print (" my age is " + age + " years ")

# output :
# enter the age : 25
# my age is 25 years


# simple calculator in python 
num1= int(input("enter the first number :"))
num2 = int(input("enter the second number :"))
print ("The sum of the given numbers is : "+ str(num1+num2))

# output : 
# enter the first number :5
# enter the second number :6
# The sum of the given numbers is : 11


# for a float number 
num1= float(input("enter the first number :"))
num2 = float(input("enter the second number :"))
result= num1+num2
print(" the sum of the number is  :"+ str(result))

#output :
# enter the first number :5.5
# enter the second number :6.5
# the sum of the number is  :12.0


# one is float and another is int
num3 = int(input("enter the first number :"))
num4 = float(input("enter the second number :"))
result = int(num3)+float(num4)
print(" the sum of the number is  :"+ str(result))

# output : 
# enter the first number :5
# enter the second number :6.5
#     the sum of the number is  :11.5

# the result will print the float output bcoz the float number is added to the int number





