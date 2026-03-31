

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if len(nums) == 1 or k == 1:
            return nums
        
        if len(nums) == 1 or k == 1 or k == len(nums):
            return [max(nums)]
        
        res = []
        l = 0
        for r in range(k-1, len(nums)):
            window_nums = nums[l:r+1]
            res.append(max(window_nums))
            l += 1

        return res
