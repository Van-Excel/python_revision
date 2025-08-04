

# type
# a set of values and operations that can be applied to it
#TYPES
#- set of values and based on these values which type they belong it
#- also looking the operations that can be performed on these types
#based on the operations you are likely to perform on these set of values 
# what is the best way to store them in memory or store a collection of these values
#- the operations you are more likely to perform on these values will determine the data structure you will use



va = 2 + \
    3
print(va)

# designing functions
# in the same way we store values in variables or their references so we can reuse them in 
# multiple places we also need a variable that stores logic we might use in multiple places
# we have built in functions for common operations and user defined functions

print(abs(3 - 89)) # returns the absolute value of a number
print(pow(3 , 7)) # used to compute the power of a number-> 3 raised to the power 7

# convert fahrenheit to celcius
# logic: subtract 32 from temperature and multiply by 5/9


def convertFahrenheitToCelcius(temperature:float, *args, **kwargs):
    """_summary_

    Args:
        temperature (float): _description_
    """
    print(kwargs.get('name'))
    return (temperature-32) * 5 / 9

print(f"212 Fahrenheit is {convertFahrenheitToCelcius(temperature=212, name='van')} in celcius")
