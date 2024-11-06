# In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the i'th basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

# Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

# Given the integer array position and the integer m. Return the required force.

# Input Format
# First Parameter: An integer n
# Second Parameter: An array position
# Third Parameter: An integer m

# Output Format
# Return an integer

# Example 1
# Input: 
# 5
# 1 2 3 4 7
# 3
# Output: 
# 3
# Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.

# Example 2
# Input: 
# 6
# 5 4 3 2 1 1000000000
# 2
# Output: 
# 999999999
# Explanation: We can use baskets 1 and 1000000000.

# Constraints
# 2 <= n <= 10^5
# 1 <= position[i] <= 10^9
# All integers in position are distinct.
# 2 <= m <= n
# Expected Time Complexity- O(n*log n)
# Expected Space Complexity - O(1)
# Magnetic Force Between Two Balls - Devsnest


def twoBallsMagneticForce(n,position,m):
    position.sort()
    def canPlaceBalls(force):
        count=1
        lastPosition=position[0]
        for i in range(1,n):
            if position[i]-lastPosition >= force:
                count += 1
                lastPosition = position[i]
                if count == m:
                    return True
        return False
    low,high= 1, position[-1]-position[0]
    result = 0
    while low <= high:
        mid = (low+high) // 2
        if canPlaceBalls(mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result
n=5
position=[1,2,3,4,7]
m=3
result=twoBallsMagneticForce(n,position,m)
print("The Magnetic force between two walls:",result)
