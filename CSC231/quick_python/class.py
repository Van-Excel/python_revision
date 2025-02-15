

# class variables- variables that are associated with the class not an instance
# of the class and  it is accessible by all instances of that class

# it is created by an assignment in the class body not the init function
# after it is created,it can be seen by all instances of that class

from math import pow
class Circle:
    pi = 3.14159

    def __init__(self, r = 1):
        self. radius = r

    def area(self):
        radius = pow(self.radius, 2)
        return f'{c.__class__.pi * radius} km\u00B2'
    
    
    
c = Circle(5)
print(c.area())