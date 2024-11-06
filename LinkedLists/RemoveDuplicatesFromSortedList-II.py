# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

# Class Node:
#     data (int)
#     next (Node)
# Input Format:
# First Parameter - Node head

# Output Format:
# Return a Node.

# Example 1:
# Input:
#     1 2 3 3 4 4 5
# Output:
#     1 2 5
# "Remove-duplicates-linked-list-1"

# Example 2:
# Input:
#     1 1 1 2 3 
# Output:
#     2 3
# "Remove-duplicates-linked-list-2"

# Constraints:
# 0<= No. of nodes <= 104
# -1000 <= Node.data <= 1000
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
def removeDuplicatesII(head):
    ans = Node(0)  # Initialize dummy node
    p = ans
    prev = None
    ptr = head

    while ptr:
        if (not prev or ptr.data != prev.data) and (not ptr.next or ptr.next.data != ptr.data):
            p.next = ptr
            p = p.next
        prev = ptr
        ptr = ptr.next

    p.next = None  # Remove duplicates at the end
    return ans.next
head=Node(1,Node(2,Node(3,Node(3,Node(4,Node(4,Node(5)))))))
print("Original Linked List")
printLL(head)
print("Remove Duplicates Sorted List-II")
printLL(removeDuplicatesII(head))
