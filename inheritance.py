from chef import chef
from chinesechef import chinesechef

myChef = chef()
myChef.make_chicken()
myChef.make_special_dish()

myChineseChef = chinesechef()
myChineseChef.make_chicken()
myChineseChef.make_special_dish()
myChineseChef.make_fried_rice() 
# Output:
# the chef makes chicken
# the chef makes bbq ribs
# The chef makes a chicken
# The chef makes orange chicken
# # The chef makes fried rice


# Inheritance
# the inheritance is the process of creating a new class from the existing class
# the new class is called the child class

class chineseChef(chef):
    def make_special_dish(self):
        print("The chef makes orange chicken")
    def make_fried_rice(self):
        print("The chef makes fried rice")
