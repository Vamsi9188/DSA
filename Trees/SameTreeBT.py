# Given the roots of two binary trees p and q, write a function to check if they are the same or not. Return 1 if they are same else 0.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Class TreeNode:
#     val (int)
#     left (TreeNode)
#     right (TreeNode)
# Input Format
# First Parameter - TreeNode p

# Second Parameter - TreeNode q

# Output Format:
# Return the number.

# Example 1:
# Input: 
#     1 2 3
#     1 2 3
# Output: 1
# "1"

# Example 2
# Input:
#     1 2
#     1 null 2
# Output: 0
# "2"

# Constraints
# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104
# Expected Time Complexity: O(n)
# Expected Space Complexity: O(n)


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
root1=TreeNode(1,TreeNode(2,TreeNode(3)))
root2=TreeNode(1,TreeNode(2,TreeNode(3)))

# Printing Tree
def printTree(root):
    if not root:
        return None
    printTree(root.left)
    print(root.val)
    printTree(root.right)

# Same Tree
def sameTree(p,q):
    if (p and not q) or (not p and q):
        return False
    if not p and not q:
        return True
    if p.val!=q.val:
        return False
    return sameTree(p.left,q.left) and sameTree(p.right,q.right)

print("Printing Tree-1:")
print(printTree(root1))
print("Printing Tree-2:")
print(printTree(root2))

print("Same Tree:",sameTree(root1,root2))

def sameTree(p,q):
    if (p and not q) or (not p and q):
        return False
    if not p and not q:
        return True
    if p.val != q.val:
        return False
    return sameTree(p.left,q.left) and sameTree(p.right,q.right)

