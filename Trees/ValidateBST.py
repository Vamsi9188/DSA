# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A BST is valid only if:

# The left subtree of a node contains only nodes with keys less than the node’s key.
# The right subtree of a node contains only nodes with keys greater than the node’s key.
# Both the left and right subtrees must also be binary search trees.
# Return 1 is given tree is valid, else return 0.

# Class TreeNode:
#     val (int)
#     left (TreeNode)
#     right (TreeNode)
# Input Format:
# First Parameter - TreeNode root

# Output Format:
# Return the number.

# Example 1:
# img

# Input:
#     root = [11 7 16 3 9]
# Output:
#     1
# Example 2:
# img

# Input:
#     root = [1 -4 -2 null null -9 5]
# Output:
#     0
# Explanation:
#     The root's node value is 1 but it's right child value is -2.
# Constraints:
# The number of nodes in the tree is in the range [1,104]
# -231 <= Node.val <= 231 - 1
# Expected Time Complexity: O(N)
# Expected Space Complexity: O(N)


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

def solve(root,min,max):
    if not root:
        return 1
    if min<root.val<max:
        return solve(root.left,min,root.val-1) and solve(root.right,root.val+1,max)
    return 0

def validateBST(root):
    return solve(root,-999999999, 999999999)



root=TreeNode(11,TreeNode(7,TreeNode(3),TreeNode(9)),TreeNode(16))
print("Printing Tree")
print(printTree(root))

print("Validate BST")
print(validateBST(root))