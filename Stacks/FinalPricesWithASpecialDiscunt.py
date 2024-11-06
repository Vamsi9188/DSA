# Given the array prices where prices[i] is the price of the ith item in a shop. There is a special discount for items in the shop, if you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i], otherwise, you will not receive any discount at all.

# Return an array where the ith element is the final price you will pay for the ith item of the shop considering the special discount.

# Input Format:-
# First Parameter - number n
# Second Parameter - array price of integers of size n

# Output Format
# Return the array of integers

# Example 1
# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]

# Explanation: 
# For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4. 
# For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2. 
# For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4. 
# For items 3 and 4 you will not receive any discount at all.

# Example 2
# Input: prices = [1,2,3,4,5]
# Output: [1,2,3,4,5]
# Explanation: In this case, for all items, you will not receive any discount at all.
    
# Constraints
# 1 <= prices.length <= 105
# 1 <= prices[i] <= 103
# Expected Time Complexity : O(n)
# Expected Space Complexity : O(n)

def finalPrices(prices):
    n=len(prices)
    discArr=[]
    nse=[0]*n
    for i in range(n-1,-1,-1):
        while discArr and discArr[-1]>prices[i]:
            discArr.pop()
        if discArr:
            nse[i]=discArr[-1]
        else:
            nse[i]=0
        discArr.append(prices[i])
    return [prices[i]-nse[i] for i in range(n)]
prices=[8,4,6,2,3]
result=finalPrices(prices)
print("The Discount Array is:",result)
