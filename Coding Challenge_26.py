# DAILY CODING CHALLENGE 26
# Question asked by: FACEBOOK
# Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced
# (well-formed).
# For example, given the string "([])[]({})", you should return true.
# Given the string "([)]" or "((()", you should return false.


# Step 1: Evaluation in Stack using push pop operation
def balance(s):
    stack = []
    for char in s:
        if char in ["(", "[", "{"]:
            stack.append(char)
        else:
            # Check character is not unmatched
            if not stack:
                return False

            # Char is a closing bracket, check top of stack if it matches
            if (char == ")" and stack[-1] != "(") or \
               (char == "]" and stack[-1] != "[") or \
               (char == "}" and stack[-1] != "{"):
                return False
            stack.pop()

    return len(stack) == 0


# Step 2: Calling the main function which calls these above functions and displays the result
string1 = "([])[]({})"
string2 = "([)]"
string3 = "((()"
print(balance(string1))
print(balance(string2))
print(balance(string3))