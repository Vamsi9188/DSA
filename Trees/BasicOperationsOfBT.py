class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
root=TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode(7,TreeNode(8),TreeNode(9))))

# Printing Tree
def printTree(root):
    if not root:
        return None
    printTree(root.left)
    print(root.val)
    printTree(root.right)
print("Printing Tree:")
print(printTree(root))

# Count Nodes of a Tree
def countNodes(root):
    if not root:
        return 0
    return (countNodes(root.left)+countNodes(root.right))+1
print("Total Nodes:",countNodes(root))

# Sum of Nodes of a Tree
def sumOfNodes(root):
    sum=0
    if not root:
        return 0
    return (sumOfNodes(root.left)+sumOfNodes(root.right))+root.val
print("Sum of Nodes:",sumOfNodes(root))

sum=0
def sumNodes1(root):
    if not root:
        return 
    global sum
    sum += root.val
    sumNodes1(root.left)
    sumNodes1(root.right)
    return sum
print("Sum Nodes-1:",sumNodes1(root))


def sumNodes2(root):
    if not root:
        return 0
    return root.val+sumNodes2(root.left)+sumNodes2(root.right)
print("Sum Nodes-2:",sumNodes2(root))


# Count Leaf Nodes
def countLeafNodes(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return countLeafNodes(root.left)+countLeafNodes(root.right)
print("Count Leaf Nodes:",countLeafNodes(root))


# Sum Leaf Nodes
def sumLeafNodes(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return root.val
    return sumLeafNodes(root.left)+sumLeafNodes(root.right)
print("Sum of Leaf Nodes:",sumLeafNodes(root))