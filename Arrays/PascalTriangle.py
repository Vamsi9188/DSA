# Write a program that takes a number n as input and prints the nth row of Pascal’s triangle.

# Note: n will be a non-negative integer.

# Input Format
# First line contains the number.

# Output Format
# Print the list.

# Example 1
# Input:
#     5
# Output:
#     [1, 4, 6, 4, 1]

# Example 2
# Input:
#     1
# Output:
#     [1]
# 1

def pascalTriangle(n):
    row=[1]
    for i in range(1,n):
        row.append(row[i-1]*(n-i)//i)
    return row
n=5
result=pascalTriangle(n)
print("The Pascal Triangle:",result)


# Another approach
class Solution:
    def generate(numRows):
        triangle=[]
        for i in range(numRows):
            row=[1]*(i+1)
            for j in range(1,i):
                row[j]=triangle[i-1][j-1]+triangle[i-1][j]
            triangle.append(row)
        return triangle