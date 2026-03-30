from collections import Counter

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Solution: hash map
        # Time:     O(n)
        # Space:    O(n)
        if len(nums) == 0:
            return 0
        l = sorted(list(Counter(nums)))
        m = c = 1
        for i in range(1, len(l)):
            d = l[i] - l[i-1]
            if d > 1:
                c = 1
            else:
                c += 1
            m = max(m, c)
        return m
