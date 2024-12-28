# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.
 

# Example 1:


# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

# Example 2:

# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.
# Example 3:

# Input: root = [], key = 0
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -105 <= Node.val <= 105
# Each node has a unique value.
# root is a valid binary search tree.
# -105 <= key <= 105
 

# Follow up: Could you solve it with time complexity O(height of tree)?


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Printing the Tree in Inorder Traversal
def printTree(root):
    if not root:
        return
    printTree(root.left)
    print(root.val, end=" ")
    printTree(root.right)

# Deleting a Node in BST
def deleteNode(root, key):
    # Helper function to find the minimum node in a subtree
    def findMin(node):
        while node.left:
            node = node.left
        return node
    if not root:
        return None
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        # Node to be deleted has only one child or no child
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        # Node with two children, replace with inorder successor (smallest in right subtree)
        minNode = findMin(root.right)
        root.val = minNode.val
        root.right = deleteNode(root.right, minNode.val)
    return root

# Initial Tree Structure
root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))

# Printing Tree Before Deletion
print("Tree before deletion (Inorder):")
printTree(root)
print("\n")

# Deleting Node with value 3
root = deleteNode(root, key=3)

# Printing Tree After Deletion
print("Tree after deletion of node with value 3 (Inorder):")
printTree(root)
print("\n")

