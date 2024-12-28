# Given a BST, and a reference to a Node x in the BST. Find the Inorder Successor of the given node in the BST.
 

# Example 1:

# Input:
#       2
#     /   \
#    1     3
# K(data of x) = 2
# Output: 3 
# Explanation: 
# Inorder traversal : 1 2 3 
# Hence, inorder successor of 2 is 3.

# Example 2:

# Input:
#              20
#             /   \
#            8     22
#           / \
#          4   12
#             /  \
#            10   14
# K(data of x) = 8
# Output: 10
# Explanation:
# Inorder traversal: 4 8 10 12 14 20 22
# Hence, successor of 8 is 10.
 

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function inOrderSuccessor(). This function takes the root node and the reference node as argument and returns the node that is inOrder successor of the reference node. If there is no successor, return null value.


# Expected Time Complexity: O(Height of the BST).
# Expected Auxiliary Space: O(1).


# Constraints:
# 1 <= N <= 105, where N is number of nodes


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Tree Structure
root = TreeNode(20, TreeNode(8, TreeNode(4), TreeNode(12, TreeNode(10), TreeNode(14))), TreeNode(22))

# Function to print the Tree (Inorder Traversal)
def printTree(root):
    if not root:
        return
    printTree(root.left)
    print(root.val)
    printTree(root.right)
# Helper function to find a node with a specific value
def findNode(root, val):
    if not root or root.val == val:
        return root
    elif val < root.val:
        return findNode(root.left, val)
    else:
        return findNode(root.right, val)
# Function to find the inorder successor
def inorderSuccessor(root, x):
    # Helper function to find the minimum value node in a subtree
    def findMin(node):
        current = node
        while current.left:
            current = current.left
        return current

    # If the node has a right subtree, find the minimum in the right subtree
    if x.right:
        return findMin(x.right)

    # Otherwise, look for the successor from the root
    successor = None
    while root:
        if x.val < root.val:
            successor = root
            root = root.left
        elif x.val > root.val:
            root = root.right
        else:
            break
    return successor

# Printing Tree Before Finding Successor
print("Tree (Inorder):")
printTree(root)
# Find the node with value 8
node_to_find = findNode(root, 8)
# Finding and printing the inorder successor
if node_to_find:
    successor = inorderSuccessor(root, node_to_find)
    if successor:
        print(f"Inorder Successor of node with value {node_to_find.val} is {successor.val}")
    else:
        print(f"No inorder successor exists for node with value {node_to_find.val}")
else:
    print("Node with value 8 not found in the tree.")
