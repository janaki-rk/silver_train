# DAILY CODING CHALLENGE 1
# Question asked by: QUORA

# Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible
# anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the
# lexicographically earliest one (the first one alphabetically).

# For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is
# the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding
# three letters, but "ecarace" comes first alphabetically.
# As another example, given the string "google", you should return "elgoogle".

# Step 1:Naive Recursive Solution
# If s is already a palindrome, then just return s -- it's already the shortest palindrome we can make
# If the first character of s (let's call it a) is the same as the last, then return a + make_palindrome(s[1:-1]) + a
# If the first character of s is different from the last (let's call this b), then return the minimum between:
# a + make_palindrome(s[1:]) + a
# b + make_palindrome(s[:-1]) + b or the lexicographically earliest one if their lengths are equal.


def is_palindrome(s):
    return s == s[::-1]


def make_palindrome(s):
    if is_palindrome(s):
        return s
    if s[0] == s[-1]:
        return s[0] + make_palindrome(s[1:-1]) + s[-1]
    else:
        one = s[0] + make_palindrome(s[1:]) + s[0]
        two = s[-1] + make_palindrome(s[:-1]) + s[-1]
        if len(one) < len(two):
            return one
        elif len(one) > len(two):
            return two
        else:
            return min(one, two)


# Step 1(Alternative): Using Dynamic Programming
cache = {}


def is_palindrome_alternative1(s):
    return s == s[::-1]


def make_palindrome_alternative_1(s):
    if s in cache:
        return cache[s]

    if is_palindrome(s):
        cache[s] = s
        return s
    if s[0] == s[-1]:
        result = s[0] + make_palindrome(s[1:-1]) + s[-1]
        cache[s] = result
        return result
    else:
        one = s[0] + make_palindrome(s[1:]) + s[0]
        two = s[-1] + make_palindrome(s[:-1]) + s[-1]
        cache[s] = min(one, two)
        return min(one, two)


# Step 1(Alternative): Using 2D Tables
def make_palindrome_alternative2(s):
    if len(s) <= 1:
        return s
    table = [['' for i in range(len(s) + 1)] for j in range(len(s) + 1)]

    for i in range(len(s)):
        table[i][1] = s[i]

    for j in range(2, len(s) + 1):
        for i in range(len(s) - j + 1):
            term = s[i:i + j]
            first, last = term[0], term[-1]
            if first == last:
                table[i][j] = first + table[i + 1][j - 2] + last
            else:
                one = first + table[i + 1][j - 1] + first
                two = last + table[i][j - 1] + last
                if len(one) < len(two):
                    table[i][j] = one
                elif len(one) > len(two):
                    table[i][j] = two
                else:
                    table[i][j] = min(one, two)

    return table[0][-1]


# Step 2: Calling the main function which calls these above functions and displays the result
string = "race"
print(make_palindrome(string))
print(make_palindrome_alternative_1(string))
print(make_palindrome_alternative2(string))
