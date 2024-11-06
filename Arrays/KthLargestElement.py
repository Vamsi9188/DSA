# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 
# Constraints:

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104


import heapq
def findKthLargest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for num in nums[k:]:
        if num > heap[0]:  # If the current number is larger than the smallest in the heap
            heapq.heapreplace(heap, num)
    return heap[0]
nums=[3,2,1,5,6,4]
k=2
result=findKthLargest(nums,k)
print("The Kth Largest element in an array is:",result)
