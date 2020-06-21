# DAILY CODING CHALLENGE 21
# Question asked by: MICROSOFT
# Given a dictionary of words and a string made up of those
# words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction,
# return any of them. If there is no possible reconstruction, then return null.For example, given the set of words
# 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown',
# 'fox'].


# Step 1: greedy approach
def find_sentence(dictionary, s):
    sentence, valid = find_sentence_helper(dictionary, s)
    if valid:
        return sentence


# helper function to tell us whether the string can actually be broken up into a sentence as well,
def find_sentence_helper(dictionary, s):
    if len(s) == 0:
        return [], True

    for i in range(len(s) + 1):
        prefix, suffix = s[:i], s[i:]
        if prefix in dictionary:
            rest, valid = find_sentence_helper(dictionary, suffix)
            if valid:
                return [prefix] + rest, True
    return [], False


# Step 1(Alternative): Using dynamic programming to store repeated subcomputations
def find_sentence_alternative(s, dictionary):
    starts = {0: ''}
    for i in range(len(s) + 1):
        new_starts = starts.copy()
        for start_index, _ in starts.items():
            word = s[start_index:i]
            if word in dictionary:
                new_starts[i] = word
        starts = new_starts.copy()

    result = []
    current_length = len(s)
    if current_length not in starts:
        return None
    while current_length > 0:
        word = starts[current_length]
        current_length -= len(word)
        result.append(word)

    return list(reversed(result))


# Step 2: Calling the main function which calls these above functions and displays the result
words = ['quick', 'brown', 'the', 'fox']
string = "thequickbrownfox"
resultant = find_sentence(words, string)
resultant1 = find_sentence_alternative(string, words)
print(resultant)
print(resultant1)
