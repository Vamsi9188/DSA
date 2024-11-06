# Remove Duplicates from Sorted Array:

# Example 1:
# Input: nums=[1,1,2]
# Output: 2

# Example 2:
# Input: nums=[0,0,1,1,1,2,2,3,3,4]
# Output: 5


def removeDuplicates(nums):
    p1=0
    for ele in nums:
        if nums[p1]!=ele:
            p1 +=1
            nums[p1]=ele
    return p1+1
nums=[0,0,1,1,1,2,2,3,3,4]
# nums=[1,1,2]
result=removeDuplicates(nums)
print("The array after removing duplicates: ",result)       
        


