# For sure, the love mobiles will roll again on this summer’s street parade. Each year, the organisers decide on a fixed order for the decorated trucks. Experience taught them to keep free a side street to be able to bring the trucks into order.

# The side street is so narrow that no two cars can pass each other. Thus, the love mobile that enters the side street last must necessarily leave the side street first. Because the trucks and the ravers move up closely, a truck cannot drive back and re-enter the side street or the approach street.

# You are given the array order in which the love mobiles arrive. Return 1 if love mobiles can be re-arranged to sorted order, else return 0.

# Input Format :-
# First Parameter - number n
# Second Parameter - array order of size n

# Output :-
# Return a number

# Example 1 :-
# Input :- 
#     5
#     5 1 2 4 3
# Output :-
#     1

# Constraints :-
# n == order.length
# 1 <= n <= 105
# 1 <= order[i] <= n
# Expected Time Complexity : O(n)
# Expected Space Complexity : O(n)
# 12

def streetParade(n,order):
    st=[]
    next=1
    for ele in order:
        if ele != next:
            st.append(ele)
        else:
            next += 1
    while st:
        ele=st.pop()
        if ele==next:
            next += 1
        else:
            return 0
    return 1
n=5
order=[5,1,2,4,3]
result=streetParade(n,order)
print("The Correct Order is:",result)
