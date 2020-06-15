# DAILY CODING CHALLENGE 15
# Question asked by: FACEBOOK
# Given a stream of elements too large to store in memory, pick a random element from the stream with uniform
# probability.

# Importing the necessary libraries
import random


# Step 1: Solving using Loop variants
def stream_elements(big_stream):
    random_element = None

    for i, e in enumerate(big_stream):
        if random.randint(1, i + 1) == 1:
            random_element = e
    return random_element


# Step 2: Calling the main function which calls these above functions and displays the result
big_streamer = [22, 44, 33, 55]
print(stream_elements(big_streamer))
