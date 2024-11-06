# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
# You must find a solution with a memory complexity better than O(n2).

# Input Format :-
# First Parameter - matrix, of size n x n
# Second Parameter - k , kth element to be returned.

# Output Format :-
# Return the kth element in the sorted matrix.

# Example 1 :-
# Input:
# 3 3
# 1 5 9
# 10 11 13
# 12 13 15
# 8
# Output:  
# 13
# Explanation: 3 3 represents the size of the matrix. The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13.

# Example 2 :-
# Input: 
# 1 1
# -5
# 1
# Output:  
# -5

# Constraints :-
# n == matrix.length == matrix[i].length.
# 1 <= n <= 300.
# -109 <= matrix[i][j] <= 109.
# All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
# 1 <= k <= n2.
# Expected Time Complexity :- O( nlog( matrix[n-1][n-1] - matrix[0][0] )).
# Expected Space Complexity :- O(1).


def kthSmallest(matrix,k):
    n=len(matrix)
    def countLessEqual(x):
        count,row,col =0,n-1,0
        while row>=0 and col<n:
            if matrix[row][col]<=x:
                count += row + 1
                col += 1
            else:
                row -= 1
        return count
    low,high=matrix[0][0],matrix[n-1][n-1]
    while low<=high:
        mid=(low+high)//2
        if countLessEqual(mid) < k:
            low = mid + 1
        else:
            high = mid - 1
    
    return low
n, m = 3, 3  
matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8
result=kthSmallest(matrix,k)
print("The Kth Smallest Element:",result)
