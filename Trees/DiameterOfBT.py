# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

# Class TreeNode:
#     val (int)
#     left (TreeNode)
#     right (TreeNode)
# Input Format
# First parameter - TreeNode root

# Output Format
# Return the number

# Example 1:
# img

# Input : 
#     root = [3 9 20 null null 15 7]
# Output :
#     3
# Explanation :
#     3 is the length of the path [7 20 3 9] or [15 20 3 9].
# Example 2:
# Input :
#     root = [10 20]
# Output :
#     1
# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100
# Expected Time Complexity: O(N)
# Expected Space Complexity: O(N)


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

# Printing Tree
def printTree(root):
    if not root:
        return None
    printTree(root.left)
    print(root.val)
    printTree(root.right)

def solve(root):
    if not root:
        return 0,0
    lPath,lDia=solve(root.left)
    rPath,rDia=solve(root.right)
    path=max(lPath,rPath)+1
    dia=max(lDia,rDia,lPath+rPath+1)
    return path,dia
def diameterOfBT(root):
    path,dia=solve(root)
    return dia-1

print("Printing Tree:")
print(printTree(root))

result=diameterOfBT(root)
print(result)