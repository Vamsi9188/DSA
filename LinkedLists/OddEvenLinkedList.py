# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# Class Node:
#     data (int)
#     next (Node)
# Input Format
# First Parameter - Node head

# Output Format
# Return the Node.

# Example 1 :
# Input :
#     LinkedList : 1 2 3 4
# Output : 
#     1 3 2 4 
# Explanation : 
# Odd elements are 1, 3 and even elements  are 2, 4. Hence, resultant linked list is  1 3 2 4. 
# Example 2 :
# Input :
#     LinkedList : 1 2 3 4 5
# Output : 
#     1 3 5 2 4 
# Explanation: 
# Odd elements are 1, 3, 5 and even elements are 2, 4. Hence, resultant linked list is 1 3 5 2 4.
# Constraints :
# The number of nodes in the linked list is in the range [0, 104].
# -106 <= Node.data <= 106
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
def oddEvenLL(head):
    if not head or not head.next:
        return head
    odd=po=head
    even=pe=head.next
    i=1
    p=head.next.next
    while p:
        if i%2==1:
            po.next=p
            po=po.next
        else:
            pe.next=p
            pe=pe.next
        i+=1
        p=p.next
    pe.next=None
    po.next=even
    return odd

head=Node(1,Node(2,Node(3,Node(4,Node(5)))))
print("Original Linked List")
printLL(head)
result=oddEvenLL(head)
print("Odd Even Linked List")
printLL(result)