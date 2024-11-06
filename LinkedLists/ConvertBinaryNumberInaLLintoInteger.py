# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

# Return the decimal value of the number in the linked list.

# The most significant bit is at the head of the linked list.

 
# Example 1:


# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10
# Example 2:

# Input: head = [0]
# Output: 0
 

# Constraints:

# The Linked List is not empty.
# Number of nodes will not exceed 30.
# Each node's value is either 0 or 1.

class Node:
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next
def printLL(head):
    while head:
        print(head.data,end="-->")
        head=head.next
    print("None")
def getDecimalNumber(head):
    result = 0
    curr = head
    while curr:
        result = (result << 1) | curr.data
        curr = curr.next
    return result
head=Node(1,Node(0,Node(0,Node(1))))
print("Binay Number Linked List")
printLL(head)
print("Decimal Number")
print(getDecimalNumber(head))
