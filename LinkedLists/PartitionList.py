# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# Class Node:
#     data (int)
#     next (Node)
# Input Format:
# First Parameter - Node head

# Second Parameter - Number x

# Output Format:
# Return the Node.

# Example 1:
# Input:
#     1 4 3 2 5 2
#     3
# Output:
#     1 2 2 4 3 5
# "partition-list-1"

# Example 2:
# Input:
#     2 1
#     2
# Output:
#     1 2

# Constraints:
# 1<= No. of nodes in either list <=104
# -100 <= Node.data <=100
# -200 <= X <= 200
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
def partitionList(head,x):
    lessHead=Node(0)
    greaterHead=Node(0)
    less=lessHead
    greater=greaterHead
    curr=head
    while curr:
        if curr.data<x:
            less.next=curr
            less=less.next
        else:
            greater.next=curr
            greater=greater.next
        curr=curr.next
    less.next=greaterHead.next
    greater.next=None
    return lessHead.next
head=Node(1,Node(4,Node(3,Node(2,Node(5,Node(2))))))
print("Original Linked List")
printLL(head)
print("Partition List")
printLL(partitionList(head,x=3))