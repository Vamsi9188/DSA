# Given the head of a singly linked list, return the middle node of the linked list. If there are two middle nodes, return the second middle node.

# The linked list must retain its structure after the function returns.

# Try to complete the program in a single loop.

# Class Node:
#     data (int)
#     next (Node)
# Input Format:
# First Parameter - Node head

# Output Format:
# Return the Node.

# Example 1:
# Input:
#     1 2 7 5 8 3 2 2 9
# Output:
#     8 3 2 2 9
# Explanation:
#      The middle of the linked list is 5th node.
# Example 2:
# Input:
#     6 4 3 1 3 7 1 9
# Output:
#     3 7 1 9
# Explanation:
#     Since the list has two middle nodes, the second node is returned.
# Constraints:
# 1<= No. of nodes in either list <=104
# 1<= Node.data <= 100
# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)
# 12


class Node:
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next
def printLL(head):
    while head:
        print(head.data,end="-->")
        head=head.next
    print("None")
def middleOfTheList(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow
head=Node(1,Node(2,Node(7,Node(5,Node(8,Node(3,Node(2,Node(2,Node(9)))))))))
print("Original Linked List")
printLL(head)
print("Middle of the Linked List")
printLL(middleOfTheList(head))
