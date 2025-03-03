# Given an array arr that contains N integers. Find a contiguous non-empty subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Input Format
# First Parameter - number n
# Second Parameter - array of integers arr of size n

# Output Format
# Return the number

# Example 1:
# Input:
#     5
#     6 -3 -10 0 2
# Output:
#     180
# Explanation:
#     Subarray with maximum product
#     is [6, -3, -10] which gives the product as 180.

# Example 2:
# Input:
#     6
#     2 3 4 5 -1 0
# Output:
#     120
# Explanation:
#     Explanation: Subarray with maximum product
#     is [2, 3, 4, 5] which gives product as 120.

# Constraints:
# 1 ≤ N ≤ 2 * 104
# -10 ≤ arr[i] ≤ 10
# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)


def maxProdSubArray(n,arr):
    if n==0:
        return 0
    maxProduct=minProduct=result=arr[0]
    for i in range(1,n):
        if arr[i]<0:
            maxProduct,minProduct=minProduct,maxProduct
        maxProduct=max(arr[i],maxProduct*arr[i])
        minProduct=min(arr[i],minProduct*arr[i])
        result=max(result,maxProduct)
    return result
n=5
arr=[6,-3,-10,0,2]
result=maxProdSubArray(n,arr)
print("The Maximu Product is:",result)