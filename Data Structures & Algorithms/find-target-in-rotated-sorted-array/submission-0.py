class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            i = (r + l) // 2
            if nums[i] == target:
                return i

            if nums[i] >= nums[l]:
                if nums[i] < target or nums[l] > target:
                    l = i + 1
                else:
                    r = i - 1

            else:
                if nums[i] > target or nums[r] < target:
                    r = i - 1
                else:
                    l = i + 1

        return -1
