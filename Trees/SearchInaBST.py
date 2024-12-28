# You are given the root of a binary search tree (BST) and an integer target

# Find the node in the BST that the node’s value equals target and return the node. If such a node does not exist, return a node with value -1.

# Class TreeNode:
#     val (int)
#     left (TreeNode)
#     right (TreeNode)
# Input Format:
# First Parameter - TreeNode root

# Second Parameter - number target

# Output Format:
# Return the TreeNode.

# Example 1:
# img

# Input:
#     root = [11 7 16 3 9]
#     target = 7
# Output:
#     [7 3 9]
# Example 2:
# img

# Input:
#     root = [11 7 16 3 9]
#     target = 5
# Output:
#      [-1]
# Constraints:
# The number of nodes in this tree is in the range of [1,5 *103]
# 1 <= node.val <= 107
# root is a binary search tree.
# 1 <= target <= 107
# Expected Time Complexity: O(h), h is the height of the binary search tree.
# Expected Space Complexity: O(h), h is the height of the binary search tree.
 

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
# printing tree
def printTree(root):
    if not root:
        return None
    print(root.val)
    printTree(root.left)
    printTree(root.right)

def searchInBST(root,target):
    # if root:
    #     if root.val==val:
    #         return root
    #     if root.val<val:
    #         return searchInBST(root.right,val)
    #     return searchInBST(root.left,val)
    # return None
    while root:
        if target < root.val:
            root = root.left
        elif target > root.val:
            root = root.right
        else:
            return root
    return TreeNode(-1)

root=TreeNode(11,TreeNode(7,TreeNode(3),TreeNode(9)),TreeNode(16))
print("Printing Tree")
print(printTree(root))

print("Search In a BST")
result=searchInBST(root,5)
printTree(result)