from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
root=TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode(7)))

# InOrder 
def printInOrder(root):
    if not root:
        return None
    printInOrder(root.left)
    print(root.val)
    printInOrder(root.right)
print("In-Order Traversal:")
print(printInOrder(root))

# Pre-Order 
def printPreOrder(root):
    if not root:
        return None
    print(root.val)
    printPreOrder(root.left)
    printPreOrder(root.right)
print("Pre-Order Traversal:")
print(printPreOrder(root))

# Post-Order
def printPostOrder(root):
    if not root:
        return None
    printPostOrder(root.left)
    printPostOrder(root.right)
    print(root.val)
print("Post-Order Traversal:")
print(printPostOrder(root))

# Level-Order1
def levelOrder(root):
    if not root:
        return None
    q=deque([root])
    while q:
        ele=q.pop()
        print(ele.val)
        if ele.left:
            q.appendleft(ele.left)
        if ele.right:
            q.appendleft(ele.right)
print("Level-Order Traversal")
print(levelOrder(root))

# Level-Order2
def levelOrder2(root):
    if not root:
        return None
    q=deque([None,root])
    while q:
        ele=q.pop()
        if ele:
            print(ele.val)
            if ele.left:
                q.appendleft(ele.left)
            if ele.right:
                q.appendleft(ele.right)
        else:
            print("---")
            if q:
                q.appendleft(None)
print("Level-Order 2")
print(levelOrder2(root))

