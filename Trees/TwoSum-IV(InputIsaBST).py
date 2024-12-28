# Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.


# Example 1:

# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
# Example 2:


# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
 
# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -104 <= Node.val <= 104
# root is guaranteed to be a valid binary search tree.
# -105 <= k <= 105


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))


# Printing Tree
def printTree(root):
    if not root:
        return None
    printTree(root.left)
    print(root.val)
    printTree(root.right)

def findTarget(root,k):
    def inorder(node):
        if not node:
            return []
        return inorder(node.left)+[node.val]+inorder(node.right)
    values=inorder(root)
    left,right=0,len(values)-1
    while left<right:
        currSum=values[left]+values[right]
        if currSum==k:
            return True
        elif currSum<k:
            left += 1
        else: 
            right -= 1
    return False


print("Printing Tree:")
print(printTree(root))

print("Two Sum-IV")
print(findTarget(root,k=9))
