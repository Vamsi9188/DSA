# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Class Node:
#     data (int)
#     next (Node)
# Input Format
# First Parameter - Node head

# Output Format
# Return the Node

# Example 1:
# Input: 1 2 3 4 5 6 7 8 

# Output: 8 7 6 5 4 3 2 1
# Example 2:
# Input: 1 5 6

# Output: 6 5 1
# Constraints:
# 1 <= N <= 10^4
# -5000 <= Node.data <= 5000
# Expected Time Complexity: O(N)
# Expected Space Complexity: O(1)
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
def reverseLL(head):
    prev=None
    curr=head
    while curr:
        nextPtr=curr.next
        curr.next=prev
        prev=curr
        curr=nextPtr
    return prev
head=Node(1,Node(2,Node(3,Node(4,Node(5)))))
print("Original Linked List:")
printLL(head)
head=reverseLL(head)
print("Reversed Linked List")
printLL(head)