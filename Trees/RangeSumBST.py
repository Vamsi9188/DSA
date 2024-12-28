# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

# Class TreeNode:
#     val (int)
#     left (TreeNode)
#     right (TreeNode)
# Input Format:
# First Parameter - TreeNode root

# Second Parameter - Number low

# Third Parameter - Number high

# Output Format:
# Return the number.

# Example 1:
# img

# Input:
#     root = [10 5 15 3 7 null 18]
#     low = 7
#     high = 15
# Output:
#     32
# Example 2:
# img

# Input:
#     root = [10 5 15 3 7 13 18 1 null 6]
#     low = 6
#     high = 10
# Output:
#     23
# Constraints:
# The number of nodes in this range [1 , 2 * 104]
# 1 <= node.val <= 105
# 1 <=low <= high <= 105
# All Node.val are unique.
# Expected Time Complexity: O(N)
# Expected Space Complexity: O(N)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Printing the Tree in Inorder Traversal
def printTree(root):
    if not root:
        return
    printTree(root.left)
    print(root.val, end=" ")
    printTree(root.right)

print("Tree before deletion (Inorder):")
printTree(root)