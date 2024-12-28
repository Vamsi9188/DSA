# Given the root of a binary tree, flatten the tree into a "linked list":

# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

# Example 1:


# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
 

# Follow up: Can you flatten the tree in-place (with O(1) extra space)?


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Sample Tree Structure
root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
# Function to print the Tree (Inorder Traversal)
def printTree(root):
    if not root:
        return
    printTree(root.left)
    print(root.val, end=" ")
    printTree(root.right)

# Function to flatten the binary tree to a linked list in-place
def flattenBTtoLL(root):
    current = root
    while current:
        if current.left:
            # Find the rightmost node in the left subtree
            rightMost = current.left
            while rightMost.right:
                rightMost = rightMost.right
            # Rewire connections
            rightMost.right = current.right
            current.right = current.left
            current.left = None
        # Move to the next right node
        current = current.right
    return root

# Printing Tree Before Flattening
print("Tree (Inorder):")
printTree(root)
print("\n")
# Flattening Binary Tree to Linked List
print("Flattened Binary Tree to Linked List:")
result = flattenBTtoLL(root)
# Printing the flattened linked list
current = result
while current:
    print(current.val, end=" -> ")
    current = current.right
print("None")
