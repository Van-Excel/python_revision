

    
input_list:list[int] = [1,2,3,4,5]
def sum_greater_than(numbers:list[int], n:int) -> int:
    """
    Calculate the sum of all elements in the list that are greater than a specified value.

    This function iterates through the provided list of numbers and adds up 
    all elements that are strictly greater than the given threshold `n`.

    Args:
        numbers (list of int or float): A list of numeric values to be evaluated.
        n (int or float): The threshold value. Only numbers greater than `n` will be included in the sum.

    Returns:
        int: The sum of all elements in `numbers` that are greater than `n`.

    Example:
        >>> input_list = [1, 2, 3, 4, 5]
        >>> sum_greater_than(input_list, 3)
        9  # (4 + 5)
    """
    
    result = 0
    for number in numbers:
        if number <= n:
            continue 
        result += number
    return result

answer = sum_greater_than(input_list, 3)
print(answer)