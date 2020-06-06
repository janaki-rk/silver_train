# DAILY CODING CHALLENGE 6
# Question asked by:GOOGLE
# An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev
# fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR
# linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at
# index.

# Importing any required files and packages:
import ctypes


# Step 1: Create a class Node which would take up the data, previous element index and next element index
class Node(object):
    def __init__(self, value):
        self.value = value
        self.both = 0


# Step 2: Create an XOR_Linked List which take up two functions to add the elements and get elements at a particular
#         index
class XOR_LList(object):
    def __init__(self):
        self.head = self.tail = None
        self.__node = []  # prevention of Garbage collections

    # Step 3: Function to add elements to the liked list
    def add(self, node):
        if self.head is None:  # If the value of the head is None, then the head and tail value is being assingned to
            # Node, else the tail is assigned to power of id of node and both value in tail
            self.head = self.tail = node
        else:
            self.tail.both = id(node) ^ self.tail.both
            node.both = id(self.tail)
            self.tail = node

        self.__node.append(node)

    # Step 4: Function to get the element at a particular index
    def get(self, index):
        previous_id = 0
        node = self.head
        for i in range(index):
            next_id = previous_id ^ node.both
            if next_id:
                previous_id = id(node)
                node = get_object(next_id)
            else:
                raise IndexError("Linked List out of range")
        return node


# Step 5: Defining an object based on the passed id value
def get_object(identity):
    return ctypes.cast(identity, ctypes.py_object).value


# Step 6: Calling the main function which calls these above functions and displays the result
node_value = Node(1)
n = XOR_LList()
n.add(2)
print(n.get(0))
