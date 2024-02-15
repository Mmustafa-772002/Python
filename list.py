# list are the data structure in python that can store the data of different types
# that may be string, integer, float, boolean etc.
# list is a collection of items that are ordered and changeable.
friends = ["Ali", "Ahmed", "Asad", "Kashif"]
# this is a list of friends
print(friends)
print(friends[0])  # this will print the first element of the list
print(friends[-1])  # when negetive index is used it will start from the end of the list
print(friends[1:])  # this will print the list from the second element to the end
print(
    friends[1:3]
)  # this will print the list from the second element to the third element
friends[1] = "Abdullah"  # this will change the second element of the list
print(friends)
# list functions
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends.extend(
    lucky_numbers
)  # this will add the lucky_numbers list to the friends list
print(friends)
friends.append("Ali")  # this will add the element to the end of the list
print(friends)
friends.insert(1, "Ahmed")  # this will add the element at the specific index
print(friends)
friends.remove("Ali")  # this will remove the specific element from the list
print(friends)
friends.pop()  # this will remove the last element from the list
print(friends)
friends.pop(1)  # this will remove the element at the specific index
print(friends)
print(friends.index("Asad"))  # this will give the index of the specific element
print(friends.count("Ali"))  # this will give the count of the specific element
num = [5, 3, 1, 7, 9, 2]
num.sort()  # this will sort the list
print(num)
friends.reverse()  # this will reverse the list
print(friends)
friends2 = friends.copy()  # this will copy the list
print(friends2)
friends.clear()  # this will clear the list
print(friends)

# the functions in lists
num = [5, 3, 1, 7, 9, 2]
num.extend([4, 8])
print("extend: " + str(num))
# extend() - this will add the list to the list
num.append(10)
print("append: " + str(num))
num.append(10)
print("append: " + str(num))
# append() - this will add the element to the end of the list
num.insert(0, 0)
print("insert: " + str(num))
# insert() - this will add the element at the specific index
num.remove(4)
print("remove : " + str(num))
# remove() - this will remove the specific element from the list
num.pop(7)
print("pop : " + str(num))
# pop() - this will remove the element from the list
a = num.index(10)
print("index: " + str(a))
# index() - this will give the index of the specific element
a = num.count(10)
print("count: " + str(a))
# count() - this will give the count of the specific element
num.sort()
print("sort: " + str(num))
# sort() - this will sort the list
num.reverse()
print("reverse: " + str(num))

# reverse() - this will reverse the list
num2 = num.copy()
print("copy: " + str(num2))
# copy() - this will copy the list
num2.clear()
print("clear: " + str(num2))

# clear() - this will clear the list

num = [5, 3, 1, 7, 9, 2]
print(len(num))
# len() - this will give the length of the list
print(min(num))
# min() - this will give the minimum value of the list
print(max(num))
# max() - this will give the maximum value of the list
print(sum(num))
# sum() - this will give the sum of the list

# list() - this will convert the data to the list

# tuple() - this will convert the data to the tuple
# set() - this will convert the data to the set
# dict() - this will convert the data to the dictionary
# zip() - this will combine the lists
# enumerate() - this will give the index and the value of the list
# all() - this will return true if all the elements are true
# any() - this will return true if any of the elements are true
# filter() - this will filter the elements
# map() - this will apply the function to the elements
# reduce() - this will reduce the elements
# lambda() - this will create the anonymous function
