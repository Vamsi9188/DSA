# You are given a string s containing just the characters in an order '(' , ')' , ‘{’ , ‘}’ , '[' and ']' , determine if the input string is valid. Return 1 if valid else 0 if invalid.

# An input string is said to be valid iff:

# 1.) Open brackets must be closed by the same type of brackets.
# 2.)Open brackets must be closed in the correct order.

# Input Format:
# First Parameter - String s

# Output Format:
# Return the number.

# Sample Tests
# Case1:
# Input: s = "()"
# Output: 1

# Case2:
# Input: s = "()[]{}"
# Output: 1

# Case3:
# Input: s = "(]"
# Output: 0

# Constraints:-
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}’.
# Expected Time Complexity: O(n)
# Expected Space Complexity: O(n)

def validParenthesis(str):
    stack=[]
    opening={"{","[","("}
    for c in str:
        if c in opening:
            stack.append(c)
        else:
            if not stack:
                return 0
            if (stack[-1],c)==("(",")") or (stack[-1],c)==("{","}") or (stack[-1],c)==("[","]"):
                stack.pop()
            else:
                return 0
    return 1 if not stack else 0
s="(){}[]"
result=validParenthesis(s)
print("The give string forms valid parenthesis:",result)

