# to access the character of a string, use the square brackets for slicing along with the index or indices to obtain your character or substring.
# For example :
word = " this is pyhton programming language"
print(word[6])

# output : i

# index function is used to find the index of the character in the string
print(word.index("p"))
print(word.index(" is"))
# output : 9

# replace function is used to replace the word in the string

replace = word.replace("pyhton", "java")
print(replace)
