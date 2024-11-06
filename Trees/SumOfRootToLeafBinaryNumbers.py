# You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

# The test cases are generated so that the answer fits in a 32-bits integer.

# Class TreeNode:
#     val (int)
#     left (TreeNode)
#     right (TreeNode)
# Input Format:
# First Parameter - TreeNode root

# Output Format:
# Return the number.

# Example 1:
# Input: 1 0 1 0 1 0 1
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
# "1"

# Example 2:
# Input: 0
# Output: 0
# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# Node.val is either 0 or 1.
# Expected Time Complexity: O(n)
# Expected Space Complexity: O(1)


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
root=TreeNode(1,TreeNode(0,TreeNode(1),TreeNode(0)),TreeNode(1,TreeNode(0),TreeNode(1)))

# Printing Tree
def printTree(root):
    if not root:
        return None
    printTree(root.left)
    print(root.val)
    printTree(root.right)

# Sum Of Root To Leaf Binary Numbers
def solve(root,ans):
    if root:
        ans=(2*ans)+root.val
        if not root.left and not root.right:
            return ans
        return solve(root.left,ans)+solve(root.right,ans)
    return 0
def sumOfRootToLeafBinaryNumbers(root):
    return solve(root,0)

print("Printing Tree:")
print(printTree(root))

print("Binary Number Sum:",sumOfRootToLeafBinaryNumbers(root))