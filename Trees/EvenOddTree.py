# A binary tree is named Even-Odd if it meets the following conditions:

# The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
# For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
# For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
# Given the root of a binary tree, return 1 if the binary tree is Even-Odd, otherwise return 0.

# Class TreeNode:
#     val (int)
#     left (TreeNode)
#     right (TreeNode)
# Input Format:
# First Paramter - TreeNode root

# Output Format:
# Return the number.

# Example 1:
# evenodd1

# Input: 1 10 4 3 null 7 9 12 8 6 null null 2
# Output: 1
# Explanation: The node values on each level are:
#     Level 0: [1]
#     Level 1: [10,4]
#     Level 2: [3,7,9]
#     Level 3: [12,8,6,2]
#     Since levels 0 and 2 are all odd and increasing and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.
# Example 2:
# evenodd2

# Input: 5 4 2 3 3 7
# Output: 0
# Explanation: The node values on each level are:
#     Level 0: [5]
#     Level 1: [4,2]
#     Level 2: [3,3,7]
#     Node values in level 2 must be in strictly increasing order, so the tree is not Even-Odd.
# Constraints:
# The number of nodes in the tree is in the range [1, 105].
# 1 <= Node.val <= 106
# Expected Time Complexity: O(N).
# Expected Space Complexity: O(1).

from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
root = TreeNode(1, TreeNode(10, TreeNode(4, TreeNode(3), None), TreeNode(7, TreeNode(9, TreeNode(12, TreeNode(8), TreeNode(6)), None), TreeNode(2))))

# Printing Tree
def printTree(root):
    if not root:
        return None
    printTree(root.left)
    print(root.val)
    printTree(root.right)

def solve(root):
    if not root:
        return 1
    queue = deque([root])
    level = 0
    while queue:
        level_size = len(queue)
        prev_val = None  
        for i in range(level_size):
            node = queue.popleft()
            if level % 2 == 0:
                if node.val % 2 == 0 or (prev_val is not None and node.val <= prev_val):
                    return 0
            else:
                if node.val % 2 == 1 or (prev_val is not None and node.val >= prev_val):
                    return 0
            prev_val = node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1
    return 1
print("Printing Tree:")
print(printTree(root))
result=solve(root)
print(result)

        