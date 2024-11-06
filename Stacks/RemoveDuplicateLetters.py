# Given a string s, remove duplicate letters so that every letter appears once and only once.

# You must make sure your result is the smallest in lexicographical order among all possible results.

# Input Format:
# First Parameter - String s

# Output Format:
# Return a string that is the smallest in lexicographical order among all possible results

# Example 1:
# Input: bcabc
# Output: abc

# Example 2:
# Input: devsnest
# Output: devnst

# Constraints:-
# 1 <= length of string <= 104
# string consists of lowercase English letters.
# Expected Time Complexity:- O(n)
# Expected Space Complexity: O(n)
# 12


def removeDuplicateLetters(s):
    last={}
    n=len(s)
    for i in range(n):
        last[s[i]]=i
    st=[]
    for i in range(n):
        ele=s[i]
        if ele not in st:
            while st and st[-1]>ele and last[st[-1]]>i:
                st.pop()
            st.append(ele)
    return "".join(st)
s="bcabc"
result=removeDuplicateLetters(s)
print("After removing duplicate letters:",result)

