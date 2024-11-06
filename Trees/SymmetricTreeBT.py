# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Class TreeNode:
#     val (int)
#     left (TreeNode)
#     right (TreeNode)
# Input Format
# First Parameter - TreeNode root

# Output Format
# Return the number.

# Example 1:
# Input: 1 2 2 3 4 4 3
# Output: 1
# "1"

# Example 2:
# Input: 1 2 2 null 3 null 3
# Output: 0
# "1"

# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
# Expected Time Complexity: O(n)
# Expected Space Complexity: O(n)



class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
# root=TreeNode(1,TreeNode(2,TreeNode(2),TreeNode(3)),TreeNode(4,TreeNode(4),TreeNode(3)))
root=TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(2,TreeNode(4),TreeNode(3)))

# Printing Tree
def printTree(root):
    if not root:
        return None
    printTree(root.left)
    print(root.val)
    printTree(root.right)

# Symmetric Tree
def isSymmetric(root):
    def solve(t1,t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val==t2.val) and solve(t1.left,t2.right) and solve(t1.right,t2.left)
    if not root:
        return 1
    return 1 if solve(root.left,root.right) else 0


print("Printing Tree:")
print(printTree(root))

print("Symmetric Tree:",isSymmetric(root))
