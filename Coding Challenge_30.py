# DAILY CODING CHALLENGE 30
# Question asked by: GOOGLE
# The edit distance between two strings refers to the minimum number of character insertions, deletions, and
# substitutions required to change one string to the other. For example, the edit distance between “kitten” and
# “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
# Given two strings, compute the edit distance between them


# Step 1: Logically, If either s1 or s2 are empty, then return the size of the larger of the two strings (since
# we can trivially turn an empty string into a string by inserting all its characters) Otherwise, return the minimum
# between:The edit distance between each string and the last n - 1 characters of the other plus one
# If the first character in each string is the same, then the edit distance between s1[1:] and s2[1:], otherwise the
# same edit distance + 1
def distance(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return max(len(s1), len(s2))

    return min(distance(s1[1:], s2) + 1,
               distance(s1, s2[1:]) + 1,
               distance(s1[1:], s2[1:]) if s1[0] == s2[0]
               else distance(s1[1:], s2[1:]) + 1)


# Step 1(Alternative): Using Dynamic Programming
def distance_alternative(s1, s2):
    x = len(s1) + 1 # the length of the x-coordinate
    y = len(s2) + 1 # the length of the y-coordinate

    A = [[-1 for i in range(x)] for j in range(y)]
    for i in range(x):
        A[0][i] = i

    for j in range(y):
        A[j][0] = j

    for i in range(1, y):
        for j in range(1, x):
            if s1[j- 1] == s2[i - 1]:
                A[i][j] = A[i - 1][j - 1]
            else:
                A[i][j] = min(
                        A[i - 1][j] + 1,
                        A[i][j - 1] + 1,
                        A[i - 1][j - 1] + 1
                        )
    return A[y - 1][x - 1] # return the edit distance between the two strings


# Step 2: Calling the main function which calls these above functions and displays the result
string1 = "kitten"
string2 = "sitting"
print(distance(string1,string2))
print(distance_alternative(string1,string2))
