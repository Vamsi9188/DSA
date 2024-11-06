#  FULL BINARY TREE

class TreeNode:
    def __init__(self, val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
def printTree(root):
    if not root:
        return None
    printTree(root.left)
    print(root.val)
    printTree(root.right)

# Full Binary Tree
def fullBinaryTree(root):
    # if root is None:
    #     return True
    if  not root or not root.left and not root.right:
        return True
    if root.left and root.right:
        return (fullBinaryTree(root.left) and fullBinaryTree(root.right))
    return False
# Example Usage
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
root1=TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3))
print("Printing Tree")
printTree(root1)
print("FBT : ",fullBinaryTree(root1))  # Output: True

# Perfect Binary Tree
def treeDepth(root):
    d = 0
    while root:
        d += 1
        root = root.left
    return d

def perfectBinaryTree(root, depth, level=0):
    if not root:
        return True
    if  not root.left and not root.right:
        return depth == level + 1
    if not root.left or not root.right:
        return False
    return (perfectBinaryTree(root.left, depth, level + 1) and 
            perfectBinaryTree(root.right, depth, level + 1))

# Example Usage
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)

root2=TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode(7,TreeNode("Vamsi"))))
print("Printing Tree")
printTree(root2)
depth = treeDepth(root2)
print("PBT : ",perfectBinaryTree(root2,depth)) # Output: True

#  COMPLETE BINARY TREE
def countNodes(root):
    if not root:
        return 0
    return (1 + countNodes(root.left) + countNodes(root.right))

def completeBinaryTree(root, index, numberOfNodes):
    if not root:
        return True
    if index >= numberOfNodes:
        return False
    return (completeBinaryTree(root.left, 2 * index + 1, numberOfNodes) and
            completeBinaryTree(root.right, 2 * index + 2, numberOfNodes))

# Example Usage
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)
root3=TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode("Vamsi")))
print("Printing Tree")
printTree(root3)
nodeCount = countNodes(root3)
print("CBT: ",completeBinaryTree(root3, 0, nodeCount))  # Output: True

#  BALANCED BINARY TREE
def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1

def balancedBinaryTree(root):
    if root is None:
        return True
    leftHeight = height(root.left)
    rightHeight = height(root.right)

    if abs(leftHeight - rightHeight) <= 1 and balancedBinaryTree(root.left) and balancedBinaryTree(root.right):
        return True
    return False

# Example Usage
root = TreeNode(100)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print("Printing Tree")
printTree(root)
print("BBT:",balancedBinaryTree(root))  # Output: True