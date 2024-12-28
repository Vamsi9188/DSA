# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

# Example 1:


# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
 

# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
 

# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))


# Printing Tree
def printTree(root):
    if not root:
        return None
    printTree(root.left)
    print(root.val)
    printTree(root.right)

# def solve(root,k,mem):
#     if not root:
#         return False
#     if k-root.val in mem:
#         return True
#     mem.add(root.val)
#     return solve(root.left,k,mem) or solve(root.right,k,mem)
# def kthSmallestInBST(root,k):
#     return solve(root,k,set())

def kthSmallest(root,k):
    count = 0
    result = None
    def inorder(node):
        nonlocal count,result
        if not node or result is not None:
            return
        inorder(node.left)
        count += 1
        if count == k:
            result = node.val
            return 
        inorder(node.right)
    inorder(root)
    return result

print("Printing Tree:")
print(printTree(root))

print("Kth Smallest Element")
print(kthSmallest(root,k=3))

