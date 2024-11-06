# Find the target element using Binary Search i.e more numbers are repeated then find first occurance of target

# Iterative method

def binarySearchFirstOccur(left,right,target):
    while left<=right:
        mid=(left+right)//2
        if a[mid]==target:
            if mid==0 or a[mid-1]!=target:
                return mid
            else:
                right=mid-1
        elif a[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
a=[5,7,7,7,7,8,8,9,9,17,32,32,80]
left=0
right=len(a)-1
target=32
result=binarySearchFirstOccur(left,right,target)
if result!=-1:
    print("The target element",target,"found at index",result)
else:
    print("The target element not found")


# Recursive Method
def bsFirstOccurRec(left,right,target):
    while left>right:
        return -1
    mid=(left+right)//2
    if a[mid]==target:
        if mid==0 or a[mid-1]!=target:
            return mid
        else:
            return bsFirstOccurRec(left,mid-1,target)
    elif a[mid]<target:
        return bsFirstOccurRec(mid+1,right,target)
    else:
        return bsFirstOccurRec(left,mid-1,target)
a=[3,4,4,5,5,12,12,21,21,33,45]
left=0
right=len(a)-1
target=21
result=bsFirstOccurRec(left,right,target)
if result!=-1:
    print(f"The target element {target} found at index {result}")
else:
    print("The target element not found")
