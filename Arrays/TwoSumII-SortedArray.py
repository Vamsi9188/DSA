# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

# Input Format
# First parameter - number n.
# Second parameter - array number of size n.
# Third parameter- target number

# Output Format
# Return the array of numbers.

# Example 1:
# Input: 4
#        2 7 11 15 
#        9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Example 2:
# Input: 3
#        2 3 4
#        6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

# Example 3:
# Input:  2
#        -1,0
#        -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

# Constraints:
# 2 <= numbers.length <= 3 * 104
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.
# Expected Time Complexity: O(n)
# Expected Space Complexity: O(1)

def twoSumSortArr(n,nums,target):
    l=0
    r=n-1
    while l<=r:
        curSum=nums[l]+nums[r]
        if curSum==target:
            return [l+1,r+1]
        if curSum<target:
            l += 1
        else:
            r -= 1
n=3
nums=[2,3,4]
target=6
result=twoSumSortArr(n,nums,target)
print("The values in indexes",result,"gives the sum of target",target)