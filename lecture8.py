def main():
    student = get_student()
    print(student)


def get_student():
    student = {}
    student["name"] = input("Name:")
    student["house"] = input("House:")
    return student


# using *args and **kwargs


# allows you to pass an arbitrary number of arguments to your function
def sum_numbers(*elements):

    result = 0
    for digit in elements:
        result += digit
    return result


print(sum_numbers(2, 3, 4, 5, 6))


num = [2, 3, 4, 5]
# assign first element to a
# assign second element in list to b
# collect the rest of the elements and store in a list
a, b, *second_list = num
print(second_list)
print(f" the type of second list is: {type(second_list)}")


# **kwargs is used for keyword or named arguments
# collects the keyword identifiers and values to construct a dictionary
def concatenate(**words):
    result = ""
    for word in words.values():
        result += " " + word
    for key, value in words.items():
        print(f"{key}: {value}")
    return result


sentence = concatenate(a="The", b="Man")
print(sentence)


# we can also pass in a regular dictionary
# if we pass it into a constructor
# it is also a function so it will unpack the dict into the obj
# if the keys of the dict are the same as attributes of the obj
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student('name': {self.name}, 'age': {self.age})"


graduate = {"name": "Van", "age": 34}

student1 = Student(**graduate)
print(student1)


# use the unpacking operator in a function with specific number of args
# used here, it unpacks the content of the list and assigns each variable to
# an item in the list if used in func with required num of args
print(*num)


def print_num(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)
    print("sum of unpacked values:", a + b + c + d)
    return (a, b, c, d)


# calling func
print(print_num(*num))


# split list into 3 parts
# assign first element to a
# assign 2nd element to b
# assign the last element to d
# collect the rest of the elements and assign to middle part
my_list = [1, 2, 3, 4, 5, 6]
a, b, *middle_part, d = my_list
print(middle_part)


# merging lists
first_list = [1, 2, 4, 5]
ray = ["c", "f", "n"]
third = [4, 6, 7]
complete_list = [*first_list, *ray, *third]
print(complete_list)

dict1 = {"name": "Alice", "age": 30}

dict2 = {"city": "New York", "country": "USA"}

complete_dict = {**dict1, **dict2}
print(complete_dict)


# you can use list("vanexcel")
# if it has some delimiter you can use split()

string_list = [*"Vanexcel"]
print(string_list)


if __name__ == "__main__":
    main()
