# Given a number n, generate all binary numbers with decimal values from 1 to N and return the array of binary number.

# Input Format
# First Parameter - number n.

# Output Format
# Return the array of strings.

# Example 1:
# Input: 3
# Output:  1 10 11
# Explanation:  Binary numbers from 1 to 3 are 1 , 10 and 11 .

# Example 2:
# Input: 6
# Output: 1 10 11 100 101 110
# Explanation:  Binary numbers from 1 to 6 are 1, 10, 11, 100, 101 and 110 .  

# Constraints
# 1 ≤ N ≤ 105
# Expected Time Complexity : O(N)
# Expected Space Complexity: O(N)


from collections import deque
def binaryNumbers(n):
    ans=[]
    q=deque(["1"])
    for i in range(n):
        ele=q.pop()
        ans.append(ele)
        q.appendleft(ele+"0")
        q.appendleft(ele+"1")
    return ans
# n=int(input())
n=20
result=binaryNumbers(n)
print("Binary numbers upto",n,"are:",result)
