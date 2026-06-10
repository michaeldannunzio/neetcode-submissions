class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(sorted(nums))
        counter = 0

        print(s)
