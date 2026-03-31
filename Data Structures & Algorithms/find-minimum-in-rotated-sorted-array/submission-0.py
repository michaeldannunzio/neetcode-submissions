class Solution:
    def findMin(self, nums: list[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            i = ((r - l) // 2) + l
            res = min(res, nums[i])
            if nums[i] >= nums[l]:
                l = i + 1
            else:
                r = i - 1
        return res
