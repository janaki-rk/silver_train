# DAILY CODING CHALLENGE 28
# Question asked by: AMAZON
# Represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA"
# would be encoded as "4A3B2C1D2A".


# Step 1: Encode by iterating over our input string and keeping a current count of whatever the current character is,
#         and once we encounter a different one, appending the count (as a string) and the actual character to our
#         result string.
def encode(s):
    if not s:
        return ''

    result = ''
    current_char = s[0]
    current_count = 1
    for i, char in enumerate(s, 1):
        if char == current_char:
            current_count += 1
        else:
            result += str(current_count) + current_char
            current_char = char
            current_count = 1
    result += str(current_count) + current_char
    return result


# Step 2: decode by iterating over the encoded string and checking each character for a digit. If it is,
#         then calculate the correct count, and once we find its corresponding character, extend the result
#         with the character count number of times and then reset the count.
def decode(s):
    count = 0
    result = ''
    for char in s:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            # char is alphabetic
            result += char * count
            count = 0
    return result


# Step 3: Calling the main function which calls these above functions and displays the result
string = "AAAABBBCCDAA"
encoded_string = encode(string)
decoded_string = decode(encoded_string)
print("encoded string ="+encoded_string, "decoded string ="+decoded_string,)
