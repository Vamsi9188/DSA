# Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list’s head.

# The steps of the insertion sort algorithm:

# Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
# It repeats until no input elements remain.
# Class Node:
#     data (int)
#     next (Node)
# Example 1
# Input:
#     4 2 1 3
# Output:
#     1 2 3 4
# "insertion-sort-list-1"

# Example 2
# Input:
#     -1 5 3 4 0
# Output:
#     -1 0 3 4 5
# "insertion-sort-list-2"

# Constraints
# The number of nodes in the list is in the range [1, 104]
# -5000 <= Node.data <= 5000
# Expected Time Complexity: O(n2)
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
def insertionSortList(head):
    dummy=Node(0)
    curr=head
    while curr:
        prev=dummy
        while prev.next and prev.next.data<curr.data:
            prev=prev.next
        nextNode=curr.next
        curr.next=prev.next
        prev.next=curr
        curr=nextNode
    return dummy.next
head=Node(4,Node(2,Node(1,Node(3))))
print("Original Linked List")
printLL(head)
print("Insertion Sort List")
printLL(insertionSortList(head))
