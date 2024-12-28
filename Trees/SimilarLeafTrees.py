# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

# imgFor example in the given tree above, the leaf value sequence is (6 7 4 9 8).

# Two Binary trees are considered leaf-similar in their leaf value sequence is the same.

# Return 1 if and only if the two given trees with head nodes root1 and root2 are leaf-similar else return 0.

# Class TreeNode:
#     val (int)
#     left (TreeNode)
#     right (TreeNode)
# Input Format
# First parameter - TreeNode root1

# Second Parameter - TreeNode root2

# Output Format
# Return the number.

# Example 1:
# img

# Input:
#     root1 = [3 5 1 6 2 9 8 null null 7 4]   
#     root2 = [3 5 1 6 7 4 2 null null null null null null 9 8]
# Output:
#     1
# Explanation:
#     Return 1 because both trees are leaf similar
# Example 2:
# img

# Input:
#     root1 = [1 2 3]
#     root2 = [1 3 2]
# Output:
#     0
# Explanation:
#     Returning 0 because both trees are not leaf similar
# Constraints
# The number of nodes in each tree will be in the range [1, 200].
# Both of the given trees will have values in the range [0, 200].
# Expected Time Complexity: O(N)
# Expected Space Complexity: O(h1+h2), where h1 and h2 are height of both the trees.

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
# root1 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(9), TreeNode(8)))
# root2 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(7, TreeNode(9), TreeNode(8))), TreeNode(1, TreeNode(4), TreeNode(2)))

root1 = TreeNode(1, TreeNode(2), TreeNode(3))
root2 = TreeNode(1, TreeNode(3), TreeNode(2))

# Printing Tree
def printTree(root):
    if not root:
        return None
    printTree(root.left)
    print(root.val)
    printTree(root.right)

def preOrder(root,l):
    if root:
        if not root.left and not root.right:
            l.append(root.val)
        preOrder(root.left, l)
        preOrder(root.right, l)
def leafSimilar(root1,root2):
    l1,l2=[],[]
    preOrder(root1,l1)
    preOrder(root2,l2)
    return l1==l2
print("Printing Tree1:")
print(printTree(root1))
print("Printing Tree2:")
print(printTree(root2))
result=leafSimilar(root1,root2)
print(result)