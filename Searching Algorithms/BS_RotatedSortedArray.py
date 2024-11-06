# Search in rotated sorted array using Binary Search

# Iterative Method
def bsInRotSorArr(arr,target):
    temp={val:i for i, val in enumerate(arr)}
    arr.sort()
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return temp[target]
        if arr[mid]>target:
            right=mid-1
        else:
            left=mid+1
    return -1
arr=[12,21,33,4,5,9,45]
# arr= [4,5,6,7,0,1,2]
target=21
result=bsInRotSorArr(arr,target)
if result!=-1:
    print(f"The target element {target} found at index {result}")
else:
    print("The target element not found")


# Recursive method
def bsInRotSorArr(arr,target):
    index_dict={val:i for i, val in enumerate(arr)}
    arr.sort()
    left=0
    right=len(arr)-1
    def bsInRotSorArrRec(left,right):
        while left<=right:
            mid=(left+right)//2
            if arr[mid]==target:
                return index_dict[target]
            if arr[mid]<target:
                return bsInRotSorArrRec(mid+1,right)
            return bsInRotSorArrRec(left,mid-1)
        return -1
    return bsInRotSorArrRec(left,right)
arr=[4,5,6,7,0,1,2]
target=40
result=bsInRotSorArr(arr,target)
if result!=-1:
    print(f"The target element {target} found at index {result}")
else:
    print("The target element not found")
