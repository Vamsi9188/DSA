# Find target element in unsorted array using binary search

# Iterative Method
def bsUnsorted(arr,target):
    left=0
    right=len(arr)-1
    arr.sort()
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            right=mid-1
        else:
            left=mid+1
    return -1
arr=[7,7,8,4,4,5,5,3,3,6,6]
target=8
result=bsUnsorted(arr,target)
if result!=-1:
    print(f"The target elememnt {target} found at index {result}")
else:
    print("The target element not found")


# Method 2

def binary_search(arr, target):
    index_dict = {val: i for i, val in enumerate(arr)}  # Store indices in a dictionary
    arr.sort()
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return index_dict[target]  # Return original index
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [7, 7, 8, 4, 4, 5, 5, 3, 3, 6, 6]
target = 8
result = binary_search(arr, target)

if result != -1:
    print(f"Target element {target} found at original index {result}")
else:
    print(f"Target element {target} not found")