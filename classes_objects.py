# the classes in the python are the blueprints for the objects
# the objects are the instances of the classes
# the classes are defined using the class keyword
# the objects are created using the class name followed by the parenthesis
# the objects are the instances of the classes


class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)


class person:
    name1 = "noor jahan "
    name2 = "mumtaj"


p1 = person()
print(p1.name1)
print(p1.name2)


class student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

def on_honor_roll(self):
    if self.gpa >= 3.5:
        return True
    else:   
        return False

