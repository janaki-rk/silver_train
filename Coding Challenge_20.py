# DAILY CODING CHALLENGE 20
# Question asked by: SNAPCHAT
# Given an array of time intervals (start, end) for classroom
# lectures (possibly overlapping), find the minimum number of rooms required. For example, given [(30, 75), (0, 50),
# (60, 150)], you should return 2.


# Step 1: go through each interval and check every other interval and see if it overlaps, keeping track of the
#         largest number of overlapping intervals.
def overlaps(a, b):
    start_a, end_a = a
    start_b, end_b = b
    # It doesn't overlap if it's like this:
    #   |start_a .... end_a|  <---> |start_b ... end_b|
    # or like this:
    #   |start_b .... end_b|  <---> |start_a ... end_a|
    # so return not or either of these
    return not (end_a < start_b or start_a > end_b)


def max_overlapping(intervals):
    current_max = 0
    for interval in intervals:
        num_overlapping = sum(overlaps(interval, other_interval)
            for other_interval in intervals
            if interval is not other_interval)
        current_max = max(current_max, num_overlapping)
    return current_max


# Step 1(Alternative): keep a couple variables to keep track of the maximum number of overlaps we've seen so
#                      far and the current number of overlaps.
def max_overlapping_1(intervals):
    starts = sorted(start for start, end in intervals)
    ends = sorted(end for start, end in intervals)

    current_max = 0
    current_overlap = 0
    i, j = 0, 0
    while i < len(intervals) and j < len(intervals):
        if starts[i] < ends[j]:
            current_overlap += 1
            current_max = max(current_max, current_overlap)
            i += 1
        else:
            current_overlap -= 1
            j += 1
    return current_max


# Step 2: Calling the main function which calls these above functions and displays the result
s = [(30, 75), (0, 50), (60, 150)]
print(max_overlapping(s))
print(max_overlapping_1(s))