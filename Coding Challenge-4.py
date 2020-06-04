# DAILY CODING CHALLENGE 4
# Question asked by:STRIPE
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other
# words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and
# negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.


# Step 1: Add all the numbers to a set, and then assign a counter, keep incrementing and then check if the number s
#         there int he set
def missing_integer(array):
    elements = set(array)
    i = 1
    while i in elements:
        i += 1
    return i


# Step 1: Alternative method which would sort the array, filter out the negatives, then iterate through the array and
#         return the index of the first number that doesn't match, just like before.
def missing_integer_alternative(array):
    if not array:
        return 1
    for i,element in enumerate(array):
        while i + 1 != array[i] and 0 < array[i] <= len(array):
            value = array[i]
            array[i], array[value - 1] = array[value - 1], array[i]
            if array[i] == array[value-1]:
                break
    for i, element in enumerate(array,1):
        if element != i:
            return i
    return len(array)+1


# Step 2: Calling the main function which calls these above functions and displays the result
array_list = [3, 4, -1, 1]
result = missing_integer(array_list)
result1 = missing_integer_alternative(array_list)
print(result)
print(result1)
