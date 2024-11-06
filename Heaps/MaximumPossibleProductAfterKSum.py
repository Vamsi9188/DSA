# You are given an array of non-negative integers nums and an integer K. In one operation, you may choose any element from nums and increment it by 1.

# Return the maximum product of nums after at most k operations. Since the answer may be very large, return it modulo 109 + 7. Note that you should maximize the product before taking the modulo.

# Input Format :
# First Parametet : n , size of array.
# Second Parameter : nums , array of integers.
# Third Parameter : k , number of operations.

# Output Format :
# Return the maximum product after K operations.

# Example 1:
# Input: 
# 2
# 0 4 
# 5
# Output: 
# 20
# Explanation: 
#     Increment the first number 5 times. Now nums = [5 4], with a product of 5 * 4 = 20. It can be shown that 20 is maximum product possible, so we return 20. Note that there may be other ways to increment nums to have the maximum product.
# Example 2:
# Input: 
# 4
# 6 3 3 2 
# 2
# Output: 
# 216
# Explanation: 
#     Increment the second number 1 time and increment the fourth number 1 time. Now nums = [6 4 3 3], with a product of 6 * 4 * 3 * 3 = 216. It can be shown that 216 is maximum product possible, so we return 216.
# Note that there may be other ways to increment nums to have the maximum product.
# Constraints :
# 1 <= n , k <= 105.
# 0 <= nums[i] <= 106.
# Expected Time Complexity : O(nlogn).
# Expected Space Complexity : O(n).
# You are given an array of non-negative integers nums and an integer K. In one operation, you may choose any element from nums and increment it by 1.

# Return the maximum product of nums after at most k operations. Since the answer may be very large, return it modulo 109 + 7. Note that you should maximize the product before taking the modulo.

# Input Format :
# First Parametet : n , size of array.
# Second Parameter : nums , array of integers.
# Third Parameter : k , number of operations.

# Output Format :
# Return the maximum product after K operations.

# Example 1:
# Input: 
# 2
# 0 4 
# 5
# Output: 
# 20
# Explanation: 
#     Increment the first number 5 times. Now nums = [5 4], with a product of 5 * 4 = 20. It can be shown that 20 is maximum product possible, so we return 20. Note that there may be other ways to increment nums to have the maximum product.
# Example 2:
# Input: 
# 4
# 6 3 3 2 
# 2
# Output: 
# 216
# Explanation: 
#     Increment the second number 1 time and increment the fourth number 1 time. Now nums = [6 4 3 3], with a product of 6 * 4 * 3 * 3 = 216. It can be shown that 216 is maximum product possible, so we return 216.
# Note that there may be other ways to increment nums to have the maximum product.
# Constraints :
# 1 <= n , k <= 105.
# 0 <= nums[i] <= 106.
# Expected Time Complexity : O(nlogn).
# Expected Space Complexity : O(n).


import heapq
MOD = 10**9 + 7
def maxProductAfterKOperations(n, nums, k):
    heapq.heapify(nums)
    for _ in range(k):
        smallest = heapq.heappop(nums)
        heapq.heappush(nums, smallest + 1)
    result = 1
    for num in nums:
        result = (result * num) % MOD
    return result

# Example 1
n = 2
nums = [0, 4]
k = 5
print(maxProductAfterKOperations(n, nums, k))  # Output: 20

# Example 2
n = 4
nums = [6, 3, 3, 2]
k = 2
print(maxProductAfterKOperations(n, nums, k))  # Output: 216
