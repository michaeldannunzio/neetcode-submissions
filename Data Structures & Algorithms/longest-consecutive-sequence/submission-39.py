class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Solution: set
        # Time:     O(n)
        # Space:    O(n)
        s = set(nums)
        r = 0
        for n in s:
            if n-1 not in s:
                c = 0
                while n+c in s:
                    c += 1
                r = max(r, c)
        return r
