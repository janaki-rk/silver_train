# DAILY CODING CHALLENGE 7
# Question asked by:FACEBOOK
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.

# Importing any required files and packages:
from collections import defaultdict


# Step 1: Using the primary logic of understanding that,if string starts with zero, then there's no valid encoding.
#         If the string's length is less than or equal to 1, there is only 1 encoding. If the first two digits form a
#         number
#         k that is less than or equal to 26, we can recursively count the number of encodings assuming we pick k as a
#         letter. We can also pick the first digit as a letter and count the number of encodings with this assumption.

def encode(string):
    if string.startswith('0'):
        return 0
    elif len(string) <= 1:
        return 1

    net = 0
    if int(string[:2]) <= 26:
        net += encode(string[2:])

    net += encode(string[1:])

    return net


# Step 1: Alternative Method which is been implemented using Dynamic Programming
def encode_alternative(string):
    cache = defaultdict(int)
    cache[len(string)] = 1

    for a in reversed(range(len(string))):
        if string[a].startswith('0'):
            cache[a] = 0
        elif a == len(string) - 1:
            cache[a] = 1
        else:
            if int(string[a:a + 2]) <= 26:
                cache[a] = cache[a + 2]
            cache[a] += cache[a + 1]
    return cache[0]


# Step 2: Calling the main function which calls these above functions and displays the result
message = '111'
result = encode(message)
result1 = encode_alternative(message)
print(result)
print(result1)
