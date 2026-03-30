class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        n = len(heights)
        l, r = 0, n-1
        while l < r:
            b = r - l
            h = min(heights[l], heights[r])
            a = b * h
            m = max(m, a)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return m
