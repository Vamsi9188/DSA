# Given the root of a binary tree, invert the tree, and return its root.

# Class TreeNode:
#     val (int)
#     left (TreeNode)
#     right (TreeNode)
# Input Format
# First Parameter - TreeNode root

# Output Format
# Return the TreeNode.

# Example 1:
# Input: 
#     4 2 7 1 3 6 9
# Output: 
#     4 7 2 9 6 3 1
# "1"

# Example 2:
# Input:
#     2 1 3
# Output:
#     2 3 1
# "2"

# Constraints:
# The number of nodes in the tree is in the range[1, 100].
# -100 <= Node.val <= 100
# Expected Time Complexity: O(n)
# Expected Space Complexity: O(n)


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
root=TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode(7,TreeNode(8),TreeNode(9))))

# Printing Tree
def printTree(root):
    if not root:
        return None
    printTree(root.left)
    print(root.val)
    printTree(root.right)

# Inverted Binary Tree
def invertBinaryTree(root):
    if not root:
        return root
    root.left, root.right = root.right, root.left
    invertBinaryTree(root.left)
    invertBinaryTree(root.right)
    return root

print("Printing Tree:")
print(printTree(root))
result=invertBinaryTree(root)
print("Inverted Binary Tree:",printTree(result))