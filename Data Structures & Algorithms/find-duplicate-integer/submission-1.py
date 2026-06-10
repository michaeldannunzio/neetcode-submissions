class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        candidate = count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1
        return candidate
