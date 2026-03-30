class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        # brute force solution
        # O(n^2)
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         max_profit = max(profit, max_profit)

        lowest_price_seen = math.inf
        for price in prices:
            # if current price is less than lowest price, set lowest price to current price
            # lowest price is not set, compare current price - lowest price with current max profit
            lowest_price_seen = min(lowest_price_seen, price)
            profit = price - lowest_price_seen
            max_profit = max(max_profit, profit)
        
        return max_profit
