# DAILY CODING CHALLENGE 3
# Question asked by:GOOGLE
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
# and deserialize(s), which deserializes the string back into the tree


# Step 1: The class for Node is been created defining the left, right and the data inside the same
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


# Step 2: The class tree is created, where a node is added
class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, node, value):
        if node is None:
            self.root = Node(value)
        else:
            if value < node.value:
                if not node.left:
                    node.left = Node(value)
                else:
                    self.add_node(node.left, value)
            else:
                if not node.right:
                    node.right = Node(value)
                else:
                    self.add_node(node.right, value)


# Step 3: Serialise the array, i.e.translate data structures or object state into a format that can be stored or
#         transmitted and reconstructed later
def serialize(root):
    values = []

    if root is None:
        return '#'
    return '{} {} {}'.format(root.value, serialize(root.left), serialize(root.right))


# Step 4: Deserialize so that we can get the original product
def deserialize(data):
    def helper():
        val = next(values)
        if val == '#':
            return None
        node = Node(int(val))
        node.left = helper()
        node.right = helper()
        return node

    values = iter(data.split())
    return helper()


# Step 5: Calling the main function which calls these above functions and displays the result
numbers = [int(n) for n in input().split(',')]
theTree = Tree()
for number in numbers:
    theTree.add_node(theTree.root, number)
s1 = serialize(theTree.root)
s2 = serialize(deserialize(s1))
print(s1)
print(s2)
assert s1 == s2
