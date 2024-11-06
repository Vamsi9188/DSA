# Find The Maximum Sum from SubArray: Kadane's Algorithm

# Example 1:
# Input: [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6

# Example 2:
# Input: [1]
# Output: 1

# Example 3:
# Input: [5,4,-1,7,8]
# Output: 23

def maxSubArry(nums):
    maxSum=-100000
    curSum=0
    for ele in nums:
        curSum += ele
        # maxSum=max(maxSum,curSum) 
        if curSum > maxSum:
            maxSum = curSum
        if curSum < 0:
            curSum=0
    return maxSum
nums=[5,4,-1,7,8]
result=maxSubArry(nums)
print("The Maximum sum of ",nums," are: ",result)


# For printing start and end index of MaxSum

def maxSubArray(nums):
    maxSum=-100000
    curSum=0
    mStart=mStop=None
    start=i
    n=len(nums)
    for i in range(n):
        ele=nums[i]
        curSum += ele
        if curSum > maxSum:
            maxSum = curSum
            mStart = start
            mStop = i
        if curSum < 0:
            curSum = 0
            start = i+1
    print(mStart,mStop)
    return maxSum
nums=[-2,1,-3,4,-1,2,1,-5,4]
result=maxSubArry(nums)
print("The Maximum sum of ",nums," are: ",result)


