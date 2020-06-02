# DAILY CODING CHALLENGE 2
# Question asked by:UBER
# Given an array of integers, return a new array such that each
# element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].


def array_multiply(array):
    # Step 1: Create prefix products
    pre_product = []
    for a in array:
        if pre_product:
            pre_product.append(pre_product[-1] * a)
        else:
            pre_product.append(a)

    # Step 2: Create suffix products
    post_product = []
    for a in reversed(array):
        if post_product:
            post_product.append(post_product[-1] * a)
        else:
            post_product.append(a)
    post_product = list(reversed(post_product))

    # Step 3: Create the resultant array to get the required result
    resultant = []
    for a in range(len(array)):
        if a == 0:
            resultant.append(post_product[a + 1])
        elif a == len(array) - 1:
            resultant.append(pre_product[a - 1])
        else:
            resultant.append(pre_product[a - 1] * post_product[a + 1])
    return resultant


# Step 4: Calling the main function which calls these above functions and displays the result

array_list = [1, 2, 3, 4, 5]
result = array_multiply(array_list)
print(result)
