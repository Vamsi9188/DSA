# Given an array of prices of an item. Before you sell an item you want to buy it. Find the maximum profit.

# Example 1:
# Input: Prices=[7,1,5,3,6,4]
# Output: maximum profit = 5

# Example 2:
# Input : Prices =[7,6,4,3,1]
# Output: 0

def solve(prices):
    n=len(prices)
    max_profit=0
    min_till_now=prices[0]
    for curr in range(1,n):
        profit=prices[curr]-min_till_now
        if profit>max_profit:
            max_profit=profit
        if prices[curr]<min_till_now:
            min_till_now=prices[curr]
    return max_profit
prices=[7,1,5,3,6,4]
result=solve(prices)
print("The Maximum Profit is: ",result)