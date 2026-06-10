class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        candidate = 0
        # count = 0
        for num in nums:
            if num == candidate:
                return num
            candidate = num
