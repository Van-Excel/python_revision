# classes and Objects

# a class is effectively a data type

class Circle:
    pi:float = 3.14
    
    def __init__(self, radius:int=1):
        self.radius = radius
        
    def area(self):
        print(f'value of pi is: {self.__class__.pi}')
        return self.radius * self.radius * self.__class__.pi
    

#Unlike C structures or Java classes, the data fields of an instance
# don’t need to be declared ahead of time; they can be created on the fly.
# you can create a new object or instance of the class type by calling the
# class name as a function.
circle = Circle(10)

print(f"the radius of the circle is {circle.radius} meters")
print(f'The area of the circle is: {circle.area()} metres' )


# you can initialize the fields of an instance automatically by
# including an __init__ method in the class body
# the __init__ function is run anything a new instance of the class is created
# with the new instance as its first argument (obj is arg for method)
# self is a parameter or variable. it will be set or initialized to new instance

class Rectangle:
    def __init__(self, width:float, length:float):
        self.width = width
        self.length = length
        
    def area(self):
        return self.width * self.length

rec1 = Rectangle(3,4)
print(f"area of rectangle one is: {rec1.width * rec1.length} meters")
print(rec1.area())


# __new__ method is called when python creates an uninitialized object



class Car:
    def __init__(self, model:str, year:int = 2010):
        self.model = model
        self.year = year

car = Car(model='BMW')
print(car.year)


# create a class of circles
# needs a class variable of type list which you append all created instances to
# static method called total area to calculate areas of all circles in the class variable