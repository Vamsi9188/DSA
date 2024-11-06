# Find the minimum in Rotated Sorted Array 

# Iterative Method
def minInRotSorArr(arr):
    l=0
    r=len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid] <= arr[mid-1]:
            return arr[mid]
        if arr[mid]>arr[r]:
            l=mid+1
        else:
            r=mid-1
    # return -1 
arr=[12,21,4,5,33,9,45,-4,0]
result=minInRotSorArr(arr)
print(f"The minimum element in a array {arr} is {result}")


# Recursive Method
def minInRotSorArr(nums):
    left=0
    right=len(nums)-1
    def minInRotSorArrRec(left,right):
        while left<=right:
            mid=(left+right)//2
            if (mid == 0 or nums[mid] <= nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] <= nums[mid + 1]):
                return nums[mid]
            elif nums[mid] > nums[right]:
                return minInRotSorArrRec(mid + 1, right)
            else:
                return minInRotSorArrRec(left, mid - 1)

    return minInRotSorArrRec(left, right)
        # return 
    minInRotSorArrRec(left,right)
nums = [2,5,3,0,1,7,6,9]
result=minInRotSorArr(nums)
print("The minimum element in array", nums, " is: ",result)
            
