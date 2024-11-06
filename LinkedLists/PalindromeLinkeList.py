# Given the head of a singly linked list, return 1 if it is a palindrome.

# Class Node:
#     data (int)
#     next (Node)
# Input Format
# First Parameter - LinkedList node head.

# Output Format
# Return 1 if list is palindrome, else return 0.

# Example 1 :
# Input :
#     LinkedList : 1 2 1
# Output : 
#     1
# Explanation : 
# The given linked list is 1 2 1 , which is a palindrome and Hence, the output is 1.
# Example 2 :
# Input : 
#     1 2 3 4
# Output : 
#     0 
# Explanation : 
# The given linked list is 1 2 3 4 , which is not a palindrome and Hence, the output is 0.
# Constraints:
# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
# Expected Time Complexity: O(N)
# Expected Auxialliary Space Usage: O(1) (i.e. , you should not use the recursive stack space as well).
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
def palindromeLinkeList(head):
    if not head or not head.next:
        return 1
    fast,slow=head,head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    prev=None
    while slow:
        nextNode=slow.next
        slow.next=prev
        prev=slow
        slow=nextNode
    firstHalf=prev
    secondHalf=head
    while secondHalf:
        if firstHalf.data!=secondHalf.data:
            return 0
        firstHalf=firstHalf.next
        secondHalf=secondHalf.next
    return 1
head=Node(1,Node(2,Node(0,Node(2,Node(1)))))
print("Original Linked List:")
printLL(head)
print(palindromeLinkeList(head))