# DAILY CODING CHALLENGE 14
# Question asked by: GOOGLE
# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

from random import uniform
from math import pow


# Step1: Solving the area of the circle with detailed descriptions
# 1--Set r to be 1 (the unit circle)
# 2--Randomly generate points within the square with corners (-1, -1), (1, 1), (1, -1), (-1, 1)
# 3--Keep track of the points that fall inside and outside the circle
# 4--You can check whether a point (x, y) is inside the circle if x2 + y2 < r2, which is another way of
#    representing a circle
# 5--Divide the number of points that fall inside the circle to the total number of points -- that
#    should give us an approximation of π / 4.

def generate():
    return uniform(-1, 1), uniform(-1, 1)


def is_in_circle(coordinates):
    return coordinates[0] * coordinates[0] + coordinates[1] * coordinates[1] < 1


def estimate():
    iterations = 10000000
    in_circle = 0
    for _ in range(iterations):
        if is_in_circle(generate()):
            in_circle += 1
    pi_over_four = in_circle / iterations
    return pi_over_four * 4


# Step 2: Calling the main function which calls these above functions and displays the result
a = [0, 4]
is_in_circle(a)
print(generate())
print(estimate())
