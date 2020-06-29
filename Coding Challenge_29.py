# DAILY CODING CHALLENGE 29
# Question asked by: FACEBOOK
# You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is
# unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.
# Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
# For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth
# index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.


# Step 1:Create two arrays that represent the running maximum heights, one from the left and one from the right. Then to
#        count the total capacity, we can run through the both arrays and add up the smaller of the two arrays at
#        that index.
def capacity(arr):
    n = len(arr)
    left_maxes = [0 for _ in range(n)]
    right_maxes = [0 for _ in range(n)]

    current_left_max = 0
    for i in range(n):
        current_left_max = max(current_left_max, arr[i])
        left_maxes[i] = current_left_max

    current_right_max = 0
    for i in range(n - 1, -1, -1):
        current_right_max = max(current_right_max, arr[i])
        right_maxes[i] = current_right_max

    total = 0
    for i in range(n):
        total += min(left_maxes[i], right_maxes[i]) - arr[i]
    return total


# Step 1(Alternative): We can find the largest element in the array, and then when we're looking on the left of it,
#                      we only need to keep the running total to the left (since we know the largest element on the
#                      array is on the right).And then do a similar thing, but starting from the right side.
def capacity_alternative(arr):
    if not arr:
        return 0

    total = 0
    max_i = arr.index(max(arr))

    left_max = arr[0]
    for num in arr[1:max_i]:
        total += left_max - num
        left_max = max(left_max, num)

    right_max = arr[-1]
    for num in arr[-2:max_i:-1]:
        total += right_max - num
        right_max = max(right_max, num)

    return total


# Step 2: Calling the main function which calls these above functions and displays the result
array = [3, 0, 1, 3, 0, 5]
print(capacity_alternative(array))
print(capacity(array))
