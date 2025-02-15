# classes and Objects

# a class is effectively a data type

class Circle:
    pass

#Unlike C structures or Java classes, the data fields of an instance
# don’t need to be declared ahead of time; they can be created on the fly.
# you can create a new object or instance of the class type by calling the
# class name as a function.
circle = Circle()
circle.radius = 34
print(f"the radius of the circle is {circle.radius} meters")


# you can initialize the fields of an instance automatically by
# including an __init__ method in the class body
# the __init__ function is run anything a new instance of the class is created
# with the new instance as its first argument (obj is arg for method)
# self is a parameter or variable. it will be set or initialized to new instance

class Rectangle:
    def __init__(self, width:float, length:float):
        self.width = width
        self.length = length

rec1 = Rectangle(3,4)
print(f"area of rectangle one is: {rec1.width * rec1.length} meters")

# __new__ method is called when python creates an uninitialized object
