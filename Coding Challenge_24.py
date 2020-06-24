# DAILY CODING CHALLENGE 24
# Question asked by: FACEBOOK
# Implement regular expression matching with the following special characters:

# . (period) which matches any single character
# * (asterisk) which matches zero or more of the preceding element

# That is, implement a function that takes in a string and a valid regular expression and returns whether or not the
# string matches the regular expression.
# For example, given the regular expression "ra." and the string "ray", your function should return true. The same
# regular expression on the string "raymond" should return false.


# Step 1:The basic idea then is to do the following. Let's call the string we want to match s and the regex r.

def matches_first_char(s, r):
    return s[0] == r[0] or (r[0] == '.' and len(s) > 0)


#   Base case: if r is empty, then return whether s is empty or not.
#   Otherwise: if the first thing in r is not
#              proceeded by a *, then match the first character of both r and s, and if they match, return match(r[1:],
#              s[1:]). If they don't, then return false. If the first thing in r _is_ proceeded by a *, then try
#              every suffix substring of s on r[2:] and return true if any suffix substring works.

def matches(s, r):
    if r == '':
        return s == ''

    if len(r) == 1 or r[1] != '*':
        # The first character in the regex is not proceeded by a *.
        if matches_first_char(s, r):
            return matches(s[1:], r[1:])
        else:
            return False
    else:
        # The first character is proceeded by a *.
        # First, try zero length.
        if matches(s, r[2:]):
            return True
        # If that doesn't match straight away, then try globbing more prefixes
        # until the first character of the string doesn't match anymore.
        i = 0
        while matches_first_char(s[i:], r):
            if matches(s[i + 1:], r[2:]):
                return True
            i += 1


# Step 2: Calling the main function which calls these above functions and displays the result
string_1 = "ray"
string_2 = "raymond"
regex = "ra."
print(matches(string_1,regex))
print(matches(string_2,regex))
