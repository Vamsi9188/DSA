# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.

# Input Format
# First Parameter - matrix image of size m x n
# Second Parameter - number sr
# Third Parameter - number sc
# Fourth Parameter - number newColor

# Output Format
# Return the modified matrix.

# Example 1:
# "flood-grid-1"

# Input:
#      3 3
#      1 1 1
#      1 1 0
#      1 0 1
#      1 
#      1 
#      2
# Output:
#      [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: 
# 3 3 represents the size of the matrix. From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels are connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2 because it is not 4-directionally connected to the starting pixel.
   
# Example 2:
# Input:
#     2 3
#     0 0 0
#     0 0 0
#     0 
#     0 
#     2
# Output:
#     [[2,2,2],[2,2,2]]

# Constraints:
# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], color < 216
# 0 <= sr < m
# 0 <= sc < n
# Expected Time Complexity: O(n)
# Expected Space Complexity: O(n)


from collections import deque
def floodFill(image,sr,sc,color):
    oldColor=image[sr][sc]
    if oldColor==color:
        return image
    q=deque([(sr,sc)])
    while q:
        sr,sc=q.popleft()
        image[sr][sc]=color
        if sr!=0 and image[sr-1][sc]==oldColor:
            q.append((sr-1,sc))
        if sc!=0 and image[sr][sc-1]==oldColor:
            q.append((sr,sc-1))
        if sr!=len(image)-1 and image[sr+1][sc]==oldColor:
            q.append((sr+1,sc))
        if sc!=len(image[0])-1 and image[sr][sc+1]==oldColor:
            q.append((sr,sc+1))
    return image
image=[[1,1,1],[1,1,0],[1,0,1]]
sr=1
sc=1
color=2
result=floodFill(image,sr,sc,color)
print("The Flood fill answer is:",result)