class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                return [nums[left], nums[right]]
            if s > target:
                right -= 1
            else:
                left += 1
