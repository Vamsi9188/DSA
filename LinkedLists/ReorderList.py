# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln

# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

# You may not modify the values in the list’s nodes. Only nodes themselves may be changed.

# Class Node:
#     data (int)
#     next (Node)
# Input Format
# First Parameter - Node head

# Output Format
# Return the Node

# Example 1 :
# Input :
#     LinkedList : 1 2 3
# Output : 
#     1 3 2
# Example 2 :
# Input:
#     LinkedList : 1 7 3 4
# Output : 
#     1 4 7 3
# Constraints:
# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.data <= 1000
# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)


class Node:
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next
def printLL(head):
    while head:
        print(head.data,end="-->")
        head=head.next
    print("None")
def cutInHalf(head):
    if not head or not head.next:
        return None
    slow=head
    fast=head.next
    while fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
    if fast.next:
        slow=slow.next
    head2=slow.next
    slow.next=None
    return head2

def reverse(head):
    prev,curr=None,head
    while curr:
        nextNode=curr.next
        curr.next=prev
        prev,curr=curr,nextNode
    return prev

def reorderList(head):
    head2=cutInHalf(head)
    head2=reverse(head2)
    p=head
    while p and head2:
        t=head2.next
        head2.next=p.next
        p.next=head2
        p=p.next.next
        head2=t
    return head

head=Node(1,Node(7,Node(3,Node(4))))
print("Original Linked List")
printLL(head)
print("Reorder List")
printLL(reorderList(head))