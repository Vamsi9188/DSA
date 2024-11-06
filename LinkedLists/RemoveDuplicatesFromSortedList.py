# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Example 1:

# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:

# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 
# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

class Node:
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next
def printLL(head):
    while head:
        print(head.data,end="-->")
        head=head.next
    print("None")
def removeDuplicates(head):
    curr=head
    while curr and curr.next:
        if curr.data==curr.next.data:
            curr.next=curr.next.next
        else:
            curr=curr.next
    return head
head=Node(1,Node(1,Node(2,Node(3,Node(3)))))
print("Original Linked List")
printLL(head)
print("Sorted List After Removing Duplicates")
printLL(removeDuplicates(head))
