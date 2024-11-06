# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Class Node:
#     data (int)
#     next (Node)
# Input Format
# First Parameter - Node l1

# Second Parameter - Node l2

# Output Format
# Return the head of the list which has sum of both the lists.

# Example 1 :
# Input :
#    l1 = 2 4 3 
#    l2 = 5 6 4
# Output : 
#    7 0 8
# Explanation :
#     243 
#   + 564 
# =   708  (adding left to right)
# Example 2 :
# Input :
#     l1 = 9 9 9 9 9 9 9 s
#     l2 = 9 9 9 9 
# Output :
#     8 9 9 9 0 0 0 1
# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.data <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.
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
def addTwoNumbers(l1,l2):
    carry=0
    ans=None
    p=None
    while l1 or l2 or carry:
        l1data=0
        if l1:
            l1data=l1.data
            l1=l1.next
        l2data=0
        if l2:
            l2data=l2.data
            l2=l2.next
        sum=carry+l1data+l2data
        carry=sum//10
        digit=sum%10
        if not ans:
            ans=Node(digit)
            p=ans
        else:
            p.next=Node(digit)
            p=p.next
    return ans

l1=Node(2,Node(4,Node(3)))
l2=Node(5,Node(6,Node(4)))
print("Linked List I")
printLL(l1)
print("Linked List II")
printLL(l2)
print("Add Two Numbers in LL")
printLL(addTwoNumbers(l1,l2))