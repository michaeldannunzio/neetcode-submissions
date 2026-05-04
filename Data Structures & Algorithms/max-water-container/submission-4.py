class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        l, r = 0, n-1

        while l < r:
            base = r - l
            height = min(heights[l], heights[r])
            area = base * height
            max_area = max(max_area, area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            
        return max_area
