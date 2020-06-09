# DAILY CODING CHALLENGE 9
# Question asked by: AIRBNB
# Given a list of integers, write a function that returns the
# largest sum of non-adjacent numbers. Numbers can be 0 or negative. For example, [2, 4, 6, 2, 5] should return 13,
# since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.


# Step 1: Say we used this function on our array from a[1:] and a[2:]. Then our solution should be a[1:] OR
#         a[0] + a[2:],whichever is largest. This is because choosing a[1:] precludes us from picking a[0].
def non_adjacent(array_list):
    if not array_list:
        return 0

    return max(non_adjacent(array_list[1:]), array_list[0] + non_adjacent(array_list[2:]))


# Step 1(Alternative): Use dynamic programming to store, in an array, the largest sum of non-adjacent numbers from index
#                      0 up to that point
def non_adjacent_alternative1(array_list):
    if len(array_list) <= 2:
        return max(0, max(array_list[0]))

    cache_array = [0 for a in array_list]
    cache_array[0] = max(0, array_list[0])
    cache_array[1] = max(cache_array[0], array_list[1])

    for i in range(2, len(array_list)):
        number = array_list[i]
        cache_array[i] = max(number + cache_array[i - 2], cache_array[i - 1])

    return cache_array[-1]


# Step 1(Alternative): We only ever use the last two elements of the cache when iterating through the array. This
#                      suggests that we could just get rid of most of the array and just store them as variables:
def non_adjacent_alternative2(array_list):
    if len(array_list) <= 2:
        return max(0, max(array_list[0]))

    maximum_excluding_last = max(0, array_list[0])
    maximum_including_last = max(maximum_excluding_last, array_list[1])

    for i in array_list[2:]:
        previous_maximum_including_last = maximum_including_last

        maximum_including_last = max(maximum_including_last, maximum_including_last + i)
        maximum_excluding_last = previous_maximum_including_last

    return max(maximum_including_last, maximum_excluding_last)


# Step 2: Calling the main function which calls these above functions and displays the result
array = [2, 4, 6, 2, 5]
result = non_adjacent(array)
result1 = non_adjacent_alternative1(array)
result2 = non_adjacent(array)
print(result)
print(result1)
print(result2)
