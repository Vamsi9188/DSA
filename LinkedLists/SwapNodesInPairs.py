# Given a linked list, swap every two adjacent nodes and return its head.

# You must solve the problem without modifying the values in the list’s nodes (i.e., only nodes themselves may be changed.)

# Class Node:
#     data (int)
#     next (Node)
# Input Format
# First Parameter - Node head

# Output Format
# Return the Node

# Example 1 :
# Input:
#     LinkedList :  1 2 2 4 5 6 7 8
# Output: 
#     2 1 4 2 6 5 8 7
# Explanation: 
# After swapping each pair considering (1,2), (2, 4), (5, 6).. so on as pairs, we get 2, 1, 4, 2, 6, 5, 8, 7 as a new linked list.
# Example 2:
# Input:
#     LinkedList :  1 3 4 7 9 10 1
# Output: 
#     3 1 7 4 10 9 1
# Explanation: After swapping each pair considering (1,3), (4, 7), (9, 10).. so
# on as pairs, we get 3, 1, 7, 4, 10, 9, 1 as a new linked list.
# Constraints:
# 1 ≤ N ≤ 103
# 0 <= Node.data <= 100
# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(1).


class Node:
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next
def printLL(head):
    while head:
        print(head.data,end="-->")
        head=head.next
    print("None")
def swapNodesInPairs(head):
    if not head or not head.next:
        return head
    p1,p2=head,head.next
    rest=swapNodesInPairs(p2.next)
    p2.next=p1
    p1.next=rest
    return p2

head=Node(1,Node(2,Node(2,Node(4,Node(5,Node(6,Node(7,Node(8))))))))
print("Original Linked List")
printLL(head)
print("Swap Nodes In Pairs")
printLL(swapNodesInPairs(head))