# DAILY CODING CHALLENGE 8
# Question asked by:GOOGLE
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#  / \
# 1   1


# Step1: The class for Node is been created defining the left, right and the data inside the same
class Node:
    # A utility function to create a node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Step 2:Creates the unival helper function
def univalued_helper(root, value):
    if root is None:
        return True
    if root.value == value:
        return univalued_helper(root.left, value) and univalued_helper(root.right, value)
    return False


# Checked whether the tree is unival or not
def is_univalued(root_value):
    return univalued_helper(root_value, root_value.value)


#  Provides the number of unival subtrees
def count_unival_subtrees(root_value):
    if root_value is None:
        return 0
    left = count_unival_subtrees(root_value.left)
    right = count_unival_subtrees(root_value.right)
    return 1 + left + right if is_univalued(root_value) else left + right


# Step 2 (Alternative): Provides the count of the universal subtrees
def count_unival_subtrees(root_value):
    count, _ = helper(root_value)
    return count


# Also returns number of univalued subtrees, and whether it is itself a unival subtree.
def helper(root_value):
    if root_value is None:
        return 0, True

    left_count, is_left_unival = helper(root_value.left)
    right_count, is_right_unival = helper(root_value.right)
    total_count = left_count + right_count

    if is_left_unival and is_right_unival:
        if root_value.left is not None and root_value.value != root_value.left.value:
            return total_count, False
        if root_value.right is not None and root_value.value != root_value.right.value:
            return total_count, False
        return total_count + 1, True
    return total_count, False


# Step 3: Calling the main function which calls these above functions and displays the result
root = Node(5)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(4)
root.left.right = Node(4)
root.right.right = Node(5)
is_univalued(root)
print('(', count_unival_subtrees(root), ',', is_univalued(root), ')')
print(helper(root))
