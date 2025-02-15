class Stack:
    """
    A class representing a stack data structure, which follows the Last In, First Out (LIFO) principle.
    """

    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.items = []  # Create an empty list to store stack elements

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.items == []  # Return True if the list is empty, otherwise False

    def pop(self):
        """
        Removes and returns the top element of the stack.

        Returns:
            Any: The element at the top of the stack.
        Raises:
            IndexError: If the stack is empty.
        """
        return self.items.pop()  # Remove and return the last element in the list

    def push(self, item):
        """
        Adds an element to the top of the stack.

        Args:
            item (Any): The element to be added to the stack.
        """
        self.items.append(item)  # Add the element to the end of the list

    def peek(self):
        """
        Returns the top element of the stack without removing it.

        Returns:
            Any: The element at the top of the stack.
            None: If the stack is empty.
        """
        if self.items:  # Check if the stack is not empty
            return self.items[
                len(self.items) - 1
            ]  # Return the last element in the list

    def size(self):
        """
        Returns the number of elements in the stack.

        Returns:
            int: The size of the stack.
        """
        return len(self.items)  # Return the length of the list

    # write a function rev_string that uses a stack to reverse the characters in a string


def reverse_string(string: str):
    """
    Reverses a given string using a stack.

    Args:
        string (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    # Initialize an empty list to store the reversed characters
    arrs: list[str] = []

    # Create an instance of the Stack class
    m = Stack()

    # Loop through each character in the input string
    for i in string:
        # Push each character onto the stack
        m.push(i)

    # Print the current items in the stack (for debugging purposes)
    print("items in stack:", m.items)

    # Continue popping elements from the stack until it is empty
    while not m.is_empty():
        # Pop the top element from the stack and append it to the list
        arrs.append(m.pop())

    # Print the items in the list after reversing (for debugging purposes)
    print("items in list:", arrs)

    # Join the reversed characters in the list into a single string and return it
    return "".join(arrs)


# Call the function with the string 'kofi' and print the reversed result
reverse_string("kofi")


# balanced parantheses
def is_balanced_parentheses(s):
    # Initialize an empty stack
    stack = Stack()

    # Iterate through each character in the string
    for char in s:
        # If it's an opening parenthesis, push it onto the stack
        if char == "(":
            stack.push(char)
        # If it's a closing parenthesis
        elif char == ")":
            # Check if the stack is not empty
            if stack.items:
                stack.pop()  # Remove the last opening parenthesis from the stack
            else:
                return False  # Unmatched closing parenthesis

    # After the loop, check if the stack is empty
    return stack.is_empty()


# Test cases
print(is_balanced_parentheses("((()))"))  # True
print(is_balanced_parentheses("(()"))  # False
print(is_balanced_parentheses("())"))  # False
print(is_balanced_parentheses("()()"))  # True
print(is_balanced_parentheses(")()("))  # False


#################################################################################################################



class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
