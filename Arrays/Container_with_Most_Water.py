# Given n non-negative integers a1, a2, …, an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i are at (i, ai) and (i, 0).

# Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Note: that you may not slant the container.

# Input Format
# First Parameter - number n
# Second Parameter - array arr of size n

# Output Format
# Return the number.

# Example 1:
# "1
# Input:
#     9
#     1 8 6 2 5 4 8 3 7
# Output:
#     49
# Explanation:
#     The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input:
#     2
#     1 1
# Output:
#     1

# Constraints:
# 2 <= n <= 105
# 0 <= arr[i] <= 104
# Expected Space Complexity: O(n)
# Expected Time Complexity: O(1)


def containerWithMostWater(n,arr):
    l=0
    r=n-1
    maxWater=0
    while l<=r:
        currWater=min(arr[l],arr[r])*(r-l)
        if currWater>maxWater:
            maxWater=currWater
        if arr[l]<arr[r]:
            l+=1
        else:
            r-=1
    return maxWater
n=9
arr=[1, 8, 6, 2, 5, 4, 8, 3, 7]
result=containerWithMostWater(n,arr)
print("Most water in the container is:",result)
