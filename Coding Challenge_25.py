# DAILY CODING CHALLENGE 25
# Question asked by: GOOGLE

# Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be
# smaller than the length of the list.

# Step 1 :Process to be performed
#         Set up two pointers at the head of the list (let's call them fast and slow)
#         Move fast up by k
#         Move both fast and slow together until fast reaches the end of the list
#         Now slow is at the N - kth node, remove it


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next
        return str(result)


def remove_kth_from_linked_list(head, k):
    slow, fast = head, head
    for i in range(k):
        fast = fast.next

    prev = None
    while fast:
        prev = slow
        slow = slow.next
        fast = fast.next

    prev.next = slow.next


# Step 2: Calling the main function which calls these above functions and displays the result
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head)
remove_kth_from_linked_list(head, 3)
print(head)