# You are given the heads of two sorted linked lists l1 and l2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Class Node:
#     data (int)
#     next (Node)
# Input Format:
# First Parameter - Node l1

# Second Parameter - Node l2

# Output Format:
# Return the Node

# Example 1:
# Input:
#     1 2 4 6
#     3 5 7 8
# Output:
#     1 2 3 4 5 6 7 8
# Explanation:
#     The resulting list contains pointers to all the values in ascending order.
#     2->3, 3->4, 4->5, 5->6, 6->7.
# Example 2:
# Input:
#     1 6 9 14 65 73
#     5 77
# Output:
#     1 5 6 9 14 65 73 77
# Explanation:
#     The resulting list contains pointers to all the values in ascending order.
#     1->5, 5->6, 73->77.
# Constraints:
# 0 <= N <=50
# -100 <= Node.data <= 100
# Expected Time Complexity: O(n)
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
def mergeTwoSortedLists(h1,h2):
    if not h1:
        return h2
    if not h2:
        return h1
    if h1.data<=h2.data:
        h1.next=mergeTwoSortedLists(h1.next,h2)
        return h1
    h2.next=mergeTwoSortedLists(h1,h2.next)
    return h2
h1=Node(1,Node(2,Node(3,Node(4))))
print("Linked List I")
printLL(h1)
h2=Node(5,Node(6,Node(7,Node(8))))
print("Linked List II")
printLL(h2)
head=mergeTwoSortedLists(h1,h2)
print("Merge Two Sorted Linked List")
printLL(head)
