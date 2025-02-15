
# data is stored in class variables in python
# it is all about modeling
# classes are used to define new data types.
# all data types have methods or functions to manipulate the data.



class Student:
    
    # instance variables are accessed by all methods of the class
    # instance variables must be referenced by self
    # instance variables should be initialised with constructor
    def __init__(self, id,  n, l):
        self.id = id
        self.first_name = n 
        self.last_name = l
        
    def say_name(self):
        print(f"The student with an id of {self.id} name is {self.first_name} {self.last_name}")
        

student =Student(1, 'Doug', "Stamford")
student.say_name()
y = student
y.first_name = 'Vanexcel'
print(student.first_name)
print(y.first_name)
c = y
c.first_name = 'Petr'
print(c.first_name)
print(y.first_name)
print(student.first_name)

class Dog:
    def __init__(self, breed, model):
        self. breed = breed
        self.model = model
        
    def bark(self):
        print(self.model['age'])
        
        
diffle = Dog('rotweiller', {"country": "germany", "age": 3})

diffle.bark()