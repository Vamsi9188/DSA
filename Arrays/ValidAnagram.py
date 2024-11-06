# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false
 
# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

def isAnagrams(s,t):
    if len(s)!=len(t):
        return False
    sCount={}
    tCount={}
    for char in s:
        sCount[char]=sCount.get(char,0)+1
    for char in t:
        tCount[char]=tCount.get(char,0)+1
    return sCount==tCount
s="anagram"
t="nagaram"
result=isAnagrams(s,t)
print(f"The strings {s} and {t} are Anagrams:",result)


# Another Method

def solve(s1,s2):
    if len(s1) != len(s2):
        return 0
    from collections import Counter
    return True if Counter(s1) == Counter(s2) else False
s1='cat'
s2='rat'
result=solve(s1,s2)
print(f"The strings {s1} and {s2} are Anagrams:",result)

