class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        n = len(nums)
        l = 0
        r = n - 1

        while l < r:
            if nums[l] + nums[r] == target:
                return [l,r]
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
