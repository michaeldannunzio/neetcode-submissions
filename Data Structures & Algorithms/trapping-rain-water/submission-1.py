class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        lm, rm = height[l], height[r]
        m = 0

        while l < r:
            if lm < rm:
                l += 1
                lm = max(lm, height[l])
                m += lm - height[l]
            else:
                r -= 1
                rm = max(rm, height[r])
                m += rm - height[r]
        return m
