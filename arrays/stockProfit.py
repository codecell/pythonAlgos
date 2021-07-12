# Q) https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/
'''
    time complexity - O(n)
    space complexity - O(1)
'''

def maxProfit(prices):
    profit = 0

    for indez in range(0, len(prices)):
        if indez + 1 < len(prices) and prices[indez + 1] > prices[indez]:
            profit += (prices[indez + 1] - prices[indez])

    return profit        

print(maxProfit([7,1,5,3,6,4])) # 7
print(maxProfit([1,2,3,4,5])) # 4