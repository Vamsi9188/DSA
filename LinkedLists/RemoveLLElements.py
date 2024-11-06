# Given the head of a linked list and an integer key, remove all the nodes of the linked list that has Node.data == key, and return the new head.

# Class Node:
#     data (int)
#     next (Node)
# Input Format
# First Parameter - Node head

# Second Parameter - number key

# Output Format
# Return the node.

# Example 1:
# Input:  1 2 6 7 5 7
#         7
# Output:  1 2 6 5

# Explanation:
# Here we want to delete node having value 7 , and return the List . 
# Example 2:
# Input: 5 5 5 5 5
#        5
# Output: (NULL)
# Constraints:
# The number of nodes in the list is in the range [0, 104].
# 1 <= Node.data <= 104
# 0 <= key <= 104
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
def removeLLElements(head,key):
    if not head:
        return None
    
    # head.next=removeLLElements(head.next,key)
    # if head.data==key:
    #     return head.next
    # return head

    while head and head.data==key:
        head=head.next
    curr=head
    while curr and curr.next:
        if curr.next.data==key:
            curr.next=curr.next.next
        else:
            curr=curr.next
    return head

head=Node(1,Node(2,Node(3,Node(2,Node(4,Node(5))))))
print("Original Linked List")
printLL(head)
head=removeLLElements(head,2)
print("After removing key element")
printLL(head)
