# Insert an element into sorted array using Binary Search

# Iterative Method
def inserAtPositionIter(arr,key):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==key:
            return mid
        if arr[mid]<key:
            left=mid+1
        else:
            right=mid-1
    return left
arr=[3,4,5,7,8,9,12,21]
key=10
result=inserAtPositionIter(arr,key)
if result!=-1:
    print("The key element ",key,"found at positon",result)
else:
    print("The key element not found")

# Recursive Method
def insertAtPosition(arr,key):
    left=0
    right=len(arr)-1
    def insertAtPositionRec(left,right):
        while left>right:
            return left
        mid=(left+right)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            return insertAtPositionRec(left,mid-1)
        return insertAtPositionRec(mid+1,right)
    return insertAtPositionRec(left,right)
arr=[2,3,6,8,12,21,33,45]
key=4
result=insertAtPosition(arr,key)
if result!=-1:
    print(f"The key element {key} found at position {result}")
else:
    print("The key element not found")