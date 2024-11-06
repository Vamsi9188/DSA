# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Class Node:
#     data (int)
#     next (Node)
# Input Format:
# First Parameter - Node l1

# Second Parameter - Node l2

# Output Format:
# Return the Node.

# Example 1:
# Input:
#     4
#     1 0 1 0
#     4
#     2 1 0 5
# Output:
#     3 1 1 5
# Explanation:
#     First node is 3 (1+2). Second node is 1 (0+1). Third node is 1 (1+0). Fourth node is 5 (0+5).
# Example 2:
# Input:
#     4
#     9 9 9 9
#     4
#     9 9 9 1
# Output:
#    1 9 9 9 0    
# Explanation:
#     Last node is 9+1, which is 10. Number is of two digits, so 1 is carried to the tens place and 0 becomes the last node. It adds to tens place (9+9) to become 19, again sending a carry to next node. Similarly, hundreds and thousands nodes become 9. Finally, a 1 is carried to the left to create an additional node.
# Constraints:
# 0<= No. of nodes <=100
# 0<= Node.data <=9
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

def reverse(head):
    prev,curr=None,head
    while curr:
        nextNode=curr.next
        curr.next=prev
        prev,curr=curr,nextNode
    return prev
def addTwoNumbers1(l1,l2):
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
        sum=l1data+l2data+carry
        carry=sum//10
        digit=sum%10
        if not ans:
            ans=Node(digit)
            p=ans
        else:
            p.next=Node(digit)
            p=p.next
    return ans
def addTwoNumbersII(l1,l2):
    l1,l2=reverse(l1),reverse(l2)
    ans=addTwoNumbers1(l1,l2)
    return reverse(ans)


l1=Node(1,Node(0,Node(1,Node(0))))
l2=Node(2,Node(1,Node(0,Node(5))))
print("Linked List I")
printLL(l1)
print("Linked List II")
printLL(l2)
print("Add Two Numbers-II")
printLL(addTwoNumbersII(l1,l2))