# dictionary in python is a collection of key-value pairs
# that is unordered, changeable and indexed

monthconversions = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}
# by  default, the key is the index of the value
print(monthconversions[1])
# we can also use the get method to get the value of a key
print(monthconversions.get(2))
# we can also use the get method to get the value of a key
print(monthconversions.get(13, "Not a valid key"))
print(monthconversions[4])
