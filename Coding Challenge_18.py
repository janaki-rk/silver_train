# DAILY CODING CHALLENGE 17
# Question asked by: GOOGLE
# Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of
# each sub-array of length k.
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)


# Importing the required libraries
from collections import deque


# Step 1: Take each sub-array of k length and compute their maxes.
def max_of_sub_arrays(lst, k):
    for i in range(len(lst) - k + 1):
        print(max(lst[i:i + k]), end=' ')


# Step 1(Alternative):Using a Heap
def max_of_sub_arrays1(lst, k):
    q = deque()
    for i in range(k):
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)

    # Loop invariant: q is a list of indices where their corresponding values are in descending order.
    for i in range(k, len(lst)):
        print(lst[q[0]], end=' ')
        while q and q[0] <= i - k:
            q.popleft()
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)
    print(lst[q[0]], end=' ')


# Step 4: Calling the main function which calls these above functions and displays the result
array = [10, 5, 2, 7, 8, 7]
k = 3
print(max_of_sub_arrays(array, k))
print(max_of_sub_arrays1(array, k))
