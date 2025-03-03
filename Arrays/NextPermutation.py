# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers. If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order). The replacement must be in place and use only constant extra memory.

# Given an array of integers nums of size n, find the next permutation.

# Input Format
# First Parameter - number n
# Second Parameter - array nums of size n

# Output Format
# return the array of integers.

# Example 1:
# Input:
#     3
#     1 2 3
# Output:
#     1 3 2

# Example 2:
# Input:
#     3
#     3 2 1
# Output:
#     1 2 3

# Example 3:
# Input:
#     3
#     1 1 5
# Output:
#     1 5 1
# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
# Expected Time Complexity: O(n)
# Expected Space Complexity: O(1)

def nextPermutation(n,nums):
    i=n-2
    while i>=0 and nums[i]>=nums[i+1]:
        i-=1
    if i>=0:
        j=n-1
        while nums[j]<=nums[i]:
            j-=1
        nums[i],nums[j]=nums[j],nums[i]
    nums[i+1:]=reversed(nums[i+1:])
    return nums
n=3
nums=[1,2,3]
result=nextPermutation(n,nums)
print("The next permutation:",result)