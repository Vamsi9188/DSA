# Given the root of a binary tree, return its maximum depth.

# A binary tree’s maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Class TreeNode:
#     val (int)
#     left (TreeNode)
#     right (TreeNode)
# Input Format
# First Parameter - TreeNode root

# Output Format
# Return the number

# Example 1:
# Input: 
#     3 9 20 null null 15 7
# Output: 3
# "1"

# Example 2:
# Input:
#     1 null 2
# Output: 2
# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100
# Expected Time Complexity: O(n)
# Expected Space Complexity: O(n)


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
root=TreeNode(3,TreeNode(9,TreeNode("null"),TreeNode("null")),TreeNode(20,TreeNode(15),TreeNode(7)))

# Printing Tree
def printTree(root):
    if not root:
        return None
    printTree(root.left)
    print(root.val)
    printTree(root.right)

# Maximum Depth of Binary Tree
def maxDepth(root):
    if root is None:
        return 0
    leftDepth=maxDepth(root.left)
    rightDepth=maxDepth(root.right)
    return 1+max(leftDepth,rightDepth)

print("Printing Tree:")
print(printTree(root))

print("Maximum Depth of BT:",maxDepth(root))