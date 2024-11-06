# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

# Input Format
# First parameter - number n
# Second parameter - array nums of size n.

# Output Format
# Return the array of numbers.

# Example 1:
# Input: 4
#        1 2 3 4 
# Output:  
#       [1, 3, 6, 10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

# Example 2:
# Input: 5
#        1 1 1 1 1
# Output:  
#        [1, 2, 3, 4, 5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

# Example 3:
# Input:  6
#         3 1 2 1 0 1
# Output: 
#         [3, 4, 6, 16, 17]

# Constraints:
# 1 <= n<= 1000
# -10^6 <= nums[i] <= 10^6
# Expected Time Complexity: O(n)
# Expected Space Complexity: O(1)

def runningSum(n,arr):
    result=[]
    curSum=0
    for i in range(n):
        curSum += arr[i]
        result.append(curSum)
    return result
n=6
arr=[3,1,2,1,0,1]
result=runningSum(n,arr)
print("The Running Sum of Array is:",result)
