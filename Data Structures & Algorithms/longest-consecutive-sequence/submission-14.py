class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(sorted(nums))
        counter = 1
        for i,num in enumerate(s, 1):
            if num - s[i] > 1:
                counter = 0
            counter += 1
        
        return counter
            