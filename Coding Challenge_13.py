# DAILY CODING CHALLENGE 13
# Question asked by: AMAZON
# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct
# characters. For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


# Step 1: try every possible substring of the string and check whether it contains at most k distinct characters. If
#         it does and it is greater than the current longest valid substring, then update the current one.
def longest_substring_with_k_distinct_characters(s, k):
    current_longest_substring = ''
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if len(set(substring)) <= k and len(substring) > len(current_longest_substring):
                current_longest_substring = substring
    return len(current_longest_substring)


# Step 1(Alternative): Done the same using dictionaries
def longest_substring_with_k_distinct_characters_alternative(s, k):
    if k == 0:
        return 0

    # Keep a running window
    bounds = (0, 0)
    h = {}
    max_length = 0
    for i, char in enumerate(s):
        h[char] = i
        if len(h) <= k:
            new_lower_bound = bounds[0]  # lower bound remains the same
        else:
            # otherwise, pop last occurring char
            key_to_pop = min(h, key=h.get)
            new_lower_bound = h.pop(key_to_pop) + 1

        bounds = (new_lower_bound, bounds[1] + 1)
        max_length = max(max_length, bounds[1] - bounds[0])

    return max_length


# Step 2: Calling the main function which calls these above functions and displays the result
string = "abcba"
k = 2
print(longest_substring_with_k_distinct_characters(string, k))
print(longest_substring_with_k_distinct_characters_alternative(string, k))
