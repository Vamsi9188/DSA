# Finding target element using binary search iterative method

def binarySearchIterative1(left,right,target):
    left=0
    right=len(l)
    while left <= right:
        mid = (left+right)//2
        if l[mid]==target:
            return mid
        elif l[mid]>target:
            right=mid-1
        else:
            left=mid+1
    return -1
l=[7,17,37,57,107,707,1007,7000,8007,8107,9999]
target=57
result=binarySearchIterative1(0,10,57)
if result!=-1:
    print(f"The Target element {target} found at index {result}")
else:
    print("The target element not found")

# Time Complexity : O(logn)
# Space Complexity : O(1)

# Finding target element using binary search iterative method

def binarySearchIterative2(low,high,target):
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    else:
        return -1
nums=[3,4,9,12,21,45]
target=21
result=binarySearchIterative2(0,5,21)
if result!=-1:
    print(f"The Target element {target} found at index {result}")
else:
    print("The target element not found")

# Time Complexity : O(logn)
# Space Complexity : O(1)


# NOTE:FOR ITERATIVE METHOD YOU HAVE TO USE ONLY WHILE FOR CHECKING CONDITION BUT ORDER IS ONLY SORTED ARRAY OR LIST

    