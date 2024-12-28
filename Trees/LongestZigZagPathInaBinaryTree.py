# You are given the root of a binary tree.

# A ZigZag path for a binary tree is defined as follow:

# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
# Change the direction from right to left or from left to right.
# Repeat the second and third steps until you can’t move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

# Return the longest ZigZag path contained in that tree.

# Class TreeNode:
#     val (int)
#     left (TreeNode)
#     right (TreeNode)
# Input Format
# First Parameter - TreeNode root

# Output Format
# Return the number.

# Example 1:
# img

# Input:      
#     1 null 1 1 1 null null 1 1 null 1 null null null 1 null 1

# Output: 3

# Explanation:   
#     Longest ZigZag path in blue nodes (right -> left -> right).
# Example 2:
# img

# Input:   
#     root = 1 1 1 null 1 null null 1 1 null 1

# Output: 4
# Constraints
# The number of nodes in the tree is in the range [1, 5 * 104].
# 1 <= Node.val <= 100
# Expected Time Complexity : O(n)
# Expected Space Complexity : O(n)

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
root = TreeNode(1, TreeNode(1, TreeNode(1, TreeNode(1)), TreeNode(1)), TreeNode(1, TreeNode(1, None, TreeNode(1))))

# Printing Tree
def printTree(root):
    if not root:
        return None
    printTree(root.left)
    print(root.val)
    printTree(root.right)

# def solve(root,p,isLeftChild):
#     if root:
#         if isLeftChild:
#             return max(solve(root.left,1,True),solve(root.right,p+1,False))
#         else:
#             return max(solve(root.left,p+1,True),solve(root.right,p,False))
#     return p-1
# def longestZigZag(root):
#     return solve(root,0,True)

def solve(root):
    ans = 0
    def dfs(node, direction, length):
        nonlocal ans
        if not node:
            return
        ans = max(ans, length)
        if direction == 'left':
            dfs(node.right, 'right', length + 1)
            dfs(node.left, 'left', 1)
        else:
            dfs(node.left, 'left', length + 1)
            dfs(node.right, 'right', 1)
    dfs(root.left, 'left', 1)
    dfs(root.right, 'right', 1)
    
    return ans

print("Printing Tree:")
print(printTree(root))
result=solve(root)
print(result)


