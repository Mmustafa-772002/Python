# Lists are the data structure in Python that can store data of different types,
# such as string, integer, float, boolean, etc.
# A list is a collection of items that are ordered and changeable.

# quick look at list
# append()
# extend()
# insert()
# remove()
# pop()
# index()
# len()
# sort()
# revserse()
# clear()
# copy()
# count()
# list()
# tuple()
# Dictionary()
# set()

friends = ["Ali", "Ahmed", "Asad", "Kashif"]

# This is a list of friends
print(friends)
print(friends[0])  # This will print the first element of the list
print(
    friends[-1]
)  # When negative index is used, it will start from the end of the list
print(friends[1:])  # This will print the list from the second element to the end
print(
    friends[1:3]
)  # This will print the list from the second element to the third element

friends[1] = "Abdullah"  # This will change the second element of the list
print(friends)

# List functions
num3 = [4, 8, 15, 16, 23, 42]
friends.extend(num3)  # This will add the lucky_numbers list to the friends list
print(friends)

friends.append("Ali")  # This will add the element to the end of the list
print(friends)

friends.insert(1, "Ahmed")  # This will add the element at the specific index
print(friends)

friends.remove("Ali")  # This will remove the specific element from the list
print(friends)

friends.pop()  # This will remove the last element from the list
print(friends)


print(friends.index("Asad"))  # This will give the index of the specific element
print(friends.count("Ali"))  # This will give the count of the specific element

num = [5, 3, 1, 7, 9, 2]
num.sort()  # This will sort the list
print(num)

friends.reverse()  # This will reverse the list
print(friends)

friends2 = friends.copy()  # This will copy the list
print(friends2)

friends.clear()  # This will clear the list
print(friends)

# List functions
num = [5, 3, 1, 7, 9, 2]
num.extend([4, 8])
print("extend:", num)

# append() - This will add the element to the end of the list
num.append(10)
print("append:", num)

# insert() - This will add the element at the specific index
num.insert(0, 0)
print("insert:", num)

# remove() - This will remove the specific element from the list
num.remove(4)
print("remove:", num)

# pop() - This will remove the element from the list
num.pop(7)
print("pop:", num)

# index() - This will give the index of the specific element
a = num.index(10)
print("index:", a)

# count() - This will give the count of the specific element
a = num.count(10)
print("count:", a)

# sort() - This will sort the list
num.sort()
print("sort:", num)

# reverse() - This will reverse the list
num.reverse()
print("reverse:", num)

# copy() - This will copy the list
num2 = num.copy()
print("copy:", num2)

# clear() - This will clear the list
num2.clear()
print("clear:", num2)

# Other functions
num = [5, 3, 1, 7, 9, 2]
# len() - This will give the length of the list
print("Length:", len(num))
# min() - This will give the minimum value of the list
print("Minimum:", min(num))
# max() - This will give the maximum value of the list
print("Maximum:", max(num))
# sum() - This will give the sum of the list
print("Sum:", sum(num))

# Conversion functions
data_list = [1, 2, 4, 4]
# Convert list to tuple, set, and dictionary
data_tuple = tuple(data_list)

data_set = set(data_list)
data_dict = dict(enumerate(data_list))
#  list function is used to convert the tuple, set, and dictionary into the list
print("List:", data_list) 
# tuples are the same as lists but they are immutable and cannot be changed once it is created 
print("Tuple:", data_tuple)
print("the index in tuple : " +str(data_tuple[2]))
# set is a collection of unordered and unindexed elements
print("Set:", data_set)
# Dictionary is a collection of key-value pairs 
print("Dictionary:", data_dict)


