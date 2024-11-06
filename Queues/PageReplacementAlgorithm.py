# n operating system, Page replacement algorithm are responsible to decide which page is needed to be replaced when new page comes in.

# Whenever a new page is referred and not present in memory, page fault occurs and Operating System replaces one of the existing pages with newly needed page.

# Given an array of integers pages of size n and a memory capacity capacity, return the total number of page faults.

# Note: You must find number of page faults using First In First Out (FIFO) page replacement algorithm.

# Input Format
# First Parameter - number n
# Second Parameter - array pages of size n
# Third Parameter - number capacity

# Output Format
# Return a number

# Example 1:
# Input:  6
#         1 3 0 3 5 6 
#         3
# Output: 5
# Explanation:
#      Initially all slots are empty, so when 1, 3, 0 came they are allocated to the empty slots —> 3 Page Faults.
# When 3 comes, it is already in memory so —> 0 Page Faults.
# Then 5 comes, it is not available in memory so it replaces the oldest page slot i.e 1. —> 1 Page Fault
# When 6 comes, it is not available in memory so it replaces the oldest page slot i.e 3  —> 1 Page Fault

# Example 2:
# Input: 12
#        0 2 1 6 4 0 1 0 3 1 2 1.
#        4
# Output:
#        9

# Constraints
# 1 <= n <= 106
# 1<= pages[i] <= 10
# 1<=slot <= 100
# Expected Time Complexity: O(n)
# Expected Space Complexity: O(n)
# 12
# #

from collections import deque
def pageReplacementAlgorithm(n,pages,capacity):
    q=deque()
    pageFault=0
    for page in pages:
        if page not in q:
            pageFault += 1
            q.appendleft(page)
            if len(q)>capacity:
                q.pop()
    return pageFault
n=6
pages=[1,3,0,3,5,6]
capacity=3
result=pageReplacementAlgorithm(n,pages,capacity)
print("The Page Faullt is:",result)
