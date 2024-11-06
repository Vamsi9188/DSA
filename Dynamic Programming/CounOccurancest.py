# Given a string S, return number of subsequences of the form aibjck, where i >= 1, j >=1 and k >= 1.

# Note:

# Two subsequences are considered different if the set of array indexes picked for the 2 subsequences are different.
# For large test cases, the output value will be too large, return the answer MODULO 10^9+7
# Input Format:
# First parameter: string S

# Output Format:
# Returns the Number

# Example 1:
# Input:
# s = "abbc"
# Output: 3
# Explanation: Subsequences are abc for 1st b, abc for 2nd b and abbc.
# Example 2:
# Input:
# s = "abcabc"
# Output: 7
# Explanation: Subsequences are abc, abc,
# abbc, aabc abcc, abc and abc.
# Constraints:
# 1 <= |S| <= 105
# Expected Time Complexity: O(Length of String).
# Expected Auxiliary Space: O(1)
# 12
# #

MOD = 10**9 + 7
def count_subsequences(S):
    count_a = 0
    count_ab = 0
    count_abc = 0
    
    for char in S:
        if char == 'a':
            count_a = (2 * count_a + 1) % MOD
        elif char == 'b':
            count_ab = (2 * count_ab + count_a) % MOD
        elif char == 'c':
            count_abc = (2 * count_abc + count_ab) % MOD
    
    return count_abc

# Example 1
s = "abbc"
print(count_subsequences(s))  # Output: 3
# Example 2
s = "abcabc"
print(count_subsequences(s))  # Output: 7
