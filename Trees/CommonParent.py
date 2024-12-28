# Given a binary tree, find the lowest common ancestor (LCA) of two given values of the nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Note :- A node can be an ancestor of itself.

# Class TreeNode:
#     val (int)
#     left (TreeNode)
#     right (TreeNode)
# Input Format :
# First Parameter - TreeNode root

# Second Parameter - descendant node value p

# Third Parameter - descendant node value q

# Output Format:
# Return a node as the lowest common ancestor of node p and node q

# Example 1:
# img

# Input:
#     root = [1 7 3 4 6 2 8 null null 5 9]
#     p = 6
#     q = 3
# Output:
#     1
# Explanation :
#     Path from root to p :- 1 7 6
#     Path from root to q :- 1 3
#     1 is the last common node which is ancestor of both node p and q.
# Example 2:
# img

# Input:
#     root = [1 7 3 4 6 2 8 null null 5 9]
#     p = 7
#     q = 9
# Output:
#     7
# Example 3:
# Input:
#     root = [1,2]
#     p = 1
#     q = 2
# Output:
#     1
# Constraints:
# The number of nodes in the tree is in the range [2, 1e5] .
# -1e9 <= Node.val <= 1e9
# All Node.val are unique.
# p != q
# p and q will exist in the tree.
# Expected Time Complexity: O(N)
# Expected Space Complexity: O(1).


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
root = TreeNode(1, TreeNode(7, TreeNode(4), TreeNode(6, TreeNode(5), TreeNode(9))), TreeNode(3, TreeNode(2), TreeNode(8)))

# Printing Tree
def printTree(root):
    if not root:
        return None
    printTree(root.left)
    print(root.val)
    printTree(root.right)

def commonParent(root, p, q):
    if root is None or root.val == p or root.val == q:
        return root
    leftLCA = commonParent(root.left, p, q)
    rightLCA = commonParent(root.right, p, q)
    if leftLCA and rightLCA:
        return root
    return leftLCA if leftLCA else rightLCA



print("Printing Tree:")
print(printTree(root))

result=commonParent(root,p=5,q=1)
print(result.val)