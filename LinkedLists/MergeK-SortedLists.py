# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []
 

# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.


class Node:
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next
def printLL(head):
    while head:
        print(head.data,end="-->")
        head=head.next
    print("None")
def mergeKLists(lists):
    nodes = []
    
    # Step 1: Collect all nodes
    for l in lists:
        while l:
            nodes.append(l.val)
            l = l.next
    
    # Step 2: Sort the values
    nodes.sort()
    
    # Step 3: Rebuild the linked list
    dummy = Node(0)
    current = dummy
    for val in nodes:
        current.next = Node(val)
        current = current.next
    
    return dummy.next


# head = Node([1,4,5], Node([1,3,4], Node([2,6])))
head = Node(1, Node(4, Node(5, Node(1, Node(3, Node(4, Node(2, Node(6, None))))))))
print("Original Linked List")
printLL(head)
print("The Merge K Sorted List")
print(mergeKLists(head))