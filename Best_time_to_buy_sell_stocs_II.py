class Solution:
    def maxProfit(self, prices: list[int],output = 0) -> int:
        for i in range(1,len(prices)):
            if(prices[i] > prices[i-1]):
                output += prices[i] - prices[i-1]
        return output