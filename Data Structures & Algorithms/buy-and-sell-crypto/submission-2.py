class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        mn = math.inf
        for p in prices:
            mn = min(mn, p)
            mx = max(mx, p-mn)
        return mx