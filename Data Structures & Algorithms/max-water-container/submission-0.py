class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left = 0
        right = len(heights) - 1
        width = right - left

        while left < right:
            area = min(heights[left], heights[right]) * width
            if area > result:
                result = area
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
            width -= 1
        
        return result
