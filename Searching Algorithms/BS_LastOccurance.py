# Fining the last occurance of a number positon in Binary Search

# Iterative method

def bsLastOccurIter(a,target):
    left=0
    right=len(a)-1
    result=-1
    while left<=right:
        mid=(left+right)//2
        if a[mid]==target:
            result=mid
            # mid==-1 or a[mid-1]!=target
            left=mid+1
        elif a[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return result
a=[3,4,4,5,5,12,12,21,21,33,45]
target=12
result = bsLastOccurIter(a,target)
if result!=-1:
    print("The target element",target,"found at index",result)
else:
    print("The target element not found.")


# Recursive Method
def bsLastOccurRec(a,target):
    left=0
    right=len(a)-1
    result=-1
    if left>right:
        return result
    mid=(left+right)//2
    if a[mid]==target:
        result=mid
        return bsLastOccurIter(mid+1,right,target)
    elif a[mid]>target:
        return bsLastOccurIter(left,mid-1,target)
    else:
        return bsLastOccurIter(mid+1,right,target)
a=[3,4,4,5,5,12,12,21,21,33,45,100]
target=4
result = bsLastOccurIter(a,target)
if result!=-1:
    print("The target element",target,"found at index",result)
else:
    print("The target element not found.")