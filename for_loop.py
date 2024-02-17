# for loop are used in python that are used to iterate over a sequence (list, tuple, string) or other iterable objects. 
# Iterating over a sequence is called traversal. 
# Syntax:
# for element in sequence:
#     Body of for
# Here, element is the variable that takes the value of the item inside the sequence on each iteration.

for i in range (5):
    print(i)
    
for letter in "python ":
    print(letter)
    
for i in range (0,10,2):
    print(i)
    
# to print a to z in range a to z using for loop
for i in range(97,123):
    print(chr(i))
    
for i in range(65,91):
    print(chr(i))
    
# to  gap between the letters
for i in range(65,91,2):
    print(chr(i))
    
# to print the reverse of the alphabets
for i in range(90,64,-1):
    print(chr(i))   

# to print the reverse of the alphabets
for i in range(122,96,-1):
    print(chr(i))
    
# to gap between the letters in reverse
for i in range(122,96,-2):
    print(chr(i))
    
    
frineds = ["Rolf", "Jen", "Anne"]
for friend in frineds:
    print(friend)
    
for index in range(len(frineds)):
    print(frineds[index])


for index in range(10):
    if index == 0:
        [print("first iteration")]
    else:
        print("Not first iteration")
    