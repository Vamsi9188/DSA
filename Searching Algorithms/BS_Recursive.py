# Finding target element uisng Binary Search Recursion (if condition)

def binarySearchRec1(left,right,target):
    if left>right:
        return -1
    mid=(left+right)//2
    if a[mid]==target:
        return mid
    elif a[mid]>target:
        return binarySearchRec1(left,mid-1,target)
    else:
        return binarySearchRec1(mid+1,right,target)
a=[4,5,12,21,33,45]
left=0
right=len(a)-1
target=45
result=binarySearchRec1(left,right,target)
if result!=-1:
    print("The target element",target,"found at index",result)
else:
    print("The target element not found.")


# Finding target element Using Binary Search Recursion (while condition)
def binarySearchRec2(left,right,target):
    while left>right:
        return -1
    mid=(left+right)//2
    if a[mid]==target:
        return mid
    elif a[mid]<target:
        return binarySearchRec2(mid+1,right,target)
    else:
        return binarySearchRec2(left,mid-1,target)
a=[7,17,37,57,107,707,1007,7000,8007,8107,9999]
target=12
left=0
right=len(a)-1
result=binarySearchRec2(0,10,12)
if result!=-1:
    print(f"The target element {target} found at index {result}")
else:
    print("The target element not found")

# NOTE:FOR RECURSIVE METHOD YOU HAVE TO USE BOTH IF OR WHILE FOR CHECKING CONDITION BUT ORDER IS ONLY SORTED ARRAY OR LIST