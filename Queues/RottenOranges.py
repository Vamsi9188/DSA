# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange,
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Note for C++ and Java: You should not use Pair.

# Input Format
# First Parameter - Matrix grid of size m x n

# Output Format
# Return the number

# Example 1:
# Input: 
#     3 3
#     2 1 1        
#     1 1 0
#     0 1 1
# Output: 4
# Explanation: 3 3 represents the size of the grid. Minimum number of minutes until no cell has fresh oranges is 4. 

# Example 2:
# Input:
#     3 3
#     2 1 1        
#     0 1 1
#     1 0 1
# Output: -1
# Explanation: 3 3 represents the size of the grid. The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Constraints
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1 or 2
# Expected Time Complexity: O(n2)
# Expected Space Complexity: O(n2)
# 12


from collections import deque
def rottenOranges(grid):
    q=deque()
    freshOranges=0
    n,m=len(grid),len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j]==2:
                q.appendleft((i,j,0))
            elif grid[i][j]==1:
                freshOranges += 1
    if not freshOranges:
        return 0
    if not q:
        return -1
    while True:
        roi,roj,rot=q.pop()
        if -1<roi+1<n and grid[roi+1][roj]==1:
            freshOranges -=  1
            grid[roi+1][roj] = 2
            q.appendleft((roi+1,roj,rot+1))
        if -1<roi-1<n and grid[roi-1][roj]==1:
            freshOranges -= 1
            grid[roi-1][roj]=2
            q.appendleft((roi-1,roj,rot+1))
        if  -1<roj+1<m and grid[roi][roj+1]==1:
            freshOranges -= 1
            grid[roi][roj+1]=2
            q.appendleft((roi,roj+1,rot+1))
        if -1<roj-1<m and grid[roi][roj-1]==1:
            freshOranges -= 1
            grid[roi][roj-1]=2
            q.appendleft((roi,roj-1,rot+1))
        if not q:
            return -1 if freshOranges else rot

grid=[[2,1,1],[1,1,0],[0,1,1]]
result=rottenOranges(grid)
print("The time taken for all oranges to be rotten is:",result)

