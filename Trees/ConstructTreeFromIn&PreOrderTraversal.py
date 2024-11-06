# Given two integer arrays inorder and preorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Class TreeNode:
#     val (int)
#     left (TreeNode)
#     right (TreeNode)
# Input Format
# First Parameter - number n1

# Second Parameter - number n2

# Third Parameter - Array of numbers preorder of size n1

# Fourth Parameter - Array of numbers inorder of size n2

# Output Format
# Return the TreeNode.

# Example 1
# Input :
# preorder = [3 9 20 15 7]
# inorder = [9 3 15 20 7]
# Output :
# [3 9 20 null null 15 7]

# Example 2
# Input :
# preorder = [10]
# inorder = [10]
# Output : 
# [10]

# Constraints:
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.
# Expected Time Complexity: O(N)
# Expected Space Complexity: O(N)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    # Dictionary to store the index of each value in inorder for quick access
    inorder_index_map = {value: idx for idx, value in enumerate(inorder)}

    # Initialize the index for the preorder traversal
    preorder_index = 0

    # Helper function to recursively build the tree
    def build_subtree(left, right):
        nonlocal preorder_index
        # Base case: if there are no elements to construct the tree
        if left > right:
            return None

        # Get the root value from the current position of preorder_index
        root_val = preorder[preorder_index]
        preorder_index += 1
        
        # Create the root node
        root = TreeNode(root_val)

        # Get the index of the root value in the inorder array
        inorder_root_index = inorder_index_map[root_val]

        # Recursively build the left and right subtrees
        root.left = build_subtree(left, inorder_root_index - 1)
        root.right = build_subtree(inorder_root_index + 1, right)

        return root

    # Build the tree from the full range of inorder (0 to len(inorder) - 1)
    return build_subtree(0, len(inorder) - 1)

# Example usage:
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
root = buildTree(preorder, inorder)

# This helper function can be used to print the tree in level order for testing
from collections import deque

def print_level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Trim the trailing Nones for clean output
    while result and result[-1] is None:
        result.pop()
    return result

# Output the tree in level-order format for the example
print(print_level_order(root))

# DEVSNEST

def solve(n1, n2, preorder, inorder):
    inorder_index_map = {value: idx for idx, value in enumerate(inorder)}
    preorder_index = 0
    def build_subtree(left, right):
        nonlocal preorder_index
        if left > right:
            return None
        root_val = preorder[preorder_index]
        preorder_index += 1
        root = TreeNode(root_val)
        inorder_root_index = inorder_index_map[root_val]
        root.left = build_subtree(left, inorder_root_index - 1)
        root.right = build_subtree(inorder_root_index + 1, right)
        return root
    return build_subtree(0, len(inorder) - 1)
