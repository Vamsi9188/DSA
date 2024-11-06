# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom .

# Class TreeNode:
#     val (int)
#     left (TreeNode)
#     right (TreeNode)
# Input Format
# First Parameter - TreeNode root

# Output Format
# Return the array

# Example 1:
# Input: 
#     root = [10 12 14 null 7 null 19]
# Output:
#     [10 14 19]

# Example 2:
# Input:
#     root = [5 7]
# Output:
#     [5 7]

# Constraints:
# The number of nodes in the tree is in the range [1, 100]
# -100 <= Node.val <= 100
# Expected Time Complexity: O(N)
# Expected Space Complexity: O(H), H is the height of the tree


from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def rightViewOfBT(root):
    if not root:
        return []
    rightView=[]
    q=deque([root])
    while q:
        levelSize=len(q)
        for i in range(levelSize):
            node=q.popleft()
            if i == levelSize-1:
                rightView.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return rightView
# TreeNode root=[10,12,14,"null",7,"null",19]
root = TreeNode(10, TreeNode(12, None, TreeNode(7)), TreeNode(14, None, TreeNode(19)))
result=rightViewOfBT(root)
print("The right view of Binary Tree is:",result)