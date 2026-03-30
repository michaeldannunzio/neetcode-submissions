class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        # brute force solution
        # O(n^2)
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)

        return max_profit