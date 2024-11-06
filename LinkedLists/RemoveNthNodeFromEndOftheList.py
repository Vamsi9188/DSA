# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
# a


class Node:
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next
def printLL(head):
    while head:
        print(head.data,end="-->")
        head=head.next
    print("None")
def removeNthNode(head,n):
    dummy=Node(0)
    dummy.next=head
    first=dummy
    second=dummy
    for _ in range(n+1):
        first = first.next
    while first:
        first=first.next
        second=second.next
    second.next=second.next.next
    return dummy.next     

head=Node(1,Node(2,Node(3,Node(4,Node(5)))))
print("Original Linked List")
printLL(head)
print("Remove Nth Node")
printLL(removeNthNode(head,n=2))


        # length = 0
        # current = head
        # while current:
        #     length += 1
        #     current = current.next
        # dummy = ListNode(0)
        # dummy.next = head
        # current = dummy
        # for _ in range(length - n):
        #     current = current.next
        # current.next = current.next.next
        # return dummy.next      