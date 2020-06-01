# DAILY CODING CHALLENGE 1
# Question asked by:GOOGLE
# Given a list a numbers and a number num, return whether the two numbers add up to give the num as result
# For example, given [10, 15, 3, 7] and num of 17, return true since 10 + 7 is 17.

# Importing any required files and packages:
from bisect import bisect_left


# Step1: Create a function which calls this function
def sum_two(array, k):
    for a in range(len(array)):
        for b in range(len(array)):
            if a != b and array[a] + array[b] == k:
                return True
    return False


# Step 1 :Alternative Method which calls the main function.Here we use a set which remembers the numbers you have stored
# and then checks if that set of numbers constitute to the element num
def sum_two_alternative1(array, k):
    element_list = set()
    for a in array:
        if k - a in element_list:
            return True
        element_list.add(a)
    return False


# Step 1:Alternative method which calls the main function. This involves sorting the list and then running a binary
# search on finding the element k
def sum_two_alternative2(array, k):
    array.sort()
    for a in range(len(array)):
        result_element = k - array[a]
        search = binary_search(array, result_element)
        if search == -1:
            continue
        elif search!=-1:
            return True
        elif search + 1 < len(array) and array[search + 1] == result_element:
            return True
        elif search - 1 >= 0 and array[search - 1] == result_element:
            return True
    return False


def binary_search(array, k):
    low = 0
    high = len(array)
    index = bisect_left(array, k, low, high)

    if 0 <= index < high and array[index] == k:
        return index
    return -1


# Step 2: Calling the main function which calls these above functions and displays the result
array_list = [10, 15, 3, 7]
element = 17
result = sum_two(array_list, element)
alternative_result1 = sum_two_alternative1(array_list, element)
alternative_result2 = sum_two_alternative2(array_list, element)
print(result, alternative_result1, alternative_result2)
