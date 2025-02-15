import time
# write an algorithm to add a sequence of numbers

def add_sequence(numArray):
    total = 0
    start = time.time()
    for num in numArray:
        total += num
    end = time.time()
    return total, end-start

# testing the function

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total, execution_time = add_sequence(numbers)
print(f"Total sum: {total}")
print(f"Execution time of algorithm: {execution_time} seconds")


# write an algorithm to add a sequence of numbers using recursion

def add_sequence_recursive(numArray):
    if not numArray:
        return 0
    else:
        return numArray[0] + add_sequence_recursive(numArray[1:])

# testing the recursive function

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = add_sequence_recursive(numbers)
print(f"Total sum: {total}")
#print(f"Execution time of recursive algorithm: {execution_time} seconds")