# Given an array of integers temperatures, represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Input Format:
# First parameter: an integer N, size of an array temperatures.
# Second parameter: an array temperatures of integers

# Output Format:
# Return the array of numbers.

# Example 1:
# Input: 
# 8
# 73 74 75 71 69 72 76 73
# Output: 
# 1 1 4 2 1 1 0 0

# Example 2:
# Input: 
# 4
# 30 40 50 60
# Output: 
# 1 1 1 0

# Example 3:
# Input: 
# 3
# 30 60 90
# Output: 
# 1 1 0

# Constraints:
# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100
# Time complexity : O(n)
# Space complexity : O(n)
