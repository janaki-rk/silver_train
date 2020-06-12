# DAILY CODING CHALLENGE 12
# Question asked by: AMAZON
# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N,
# write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
# For example, if N is 4, then there are 5 unique ways:
# 1, 1, 1, 1
# 2, 1,1
# 1, 2, 1
# 1, 1, 2
# 2, 2


# Step 1: f(n) = f(n - 1) + f(n - 2)- The Fibonacci sequence!
def staircase_1(value):
    if value <= 1:
        return 1
    return staircase_1(value - 1) + staircase_1(value - 2)


# Step 1 (Alternative):Iterative Computation
def staircase_2(value):
    x, y = 1, 2
    for a in range(value - 1):
        x, y = y, x + y
    return x


# Step 1 (Alternative): if X = {1, 3, 5}, then our algorithm should be f(n) = f(n - 1) + f(n - 3) + f(n - 5). If n <
#                       0, then we should return 0 since we can't start from a negative number of steps.
def staircase_3(value, A):
    if value < 0:
        return 0
    elif value == 0:
        return 1
    else:
        return sum(staircase_3(value - a, A) for a in A)


# Step 1(Alternative): Use dynamic programming
def staircase_4(value, A):
    cache = [0 for a in range(value + 1)]
    cache[0] = 1
    for s in range(1, value + 1):
        cache[s] += sum(cache[s - a] for a in A if s - a >= 0)
    return cache[value]


# Step 2: Calling the main function which calls these above functions and displays the result
m = 4
M = {1, 3, 5}
result1 = staircase_1(m)
result2 = staircase_2(m)
result3 = staircase_3(m, M)
result4 = staircase_4(m, M)
print(result1, result2, result3, result4)
