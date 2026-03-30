class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_len = 0
        for num in nums:
            if num - 1 not in s:
                current_len = 1
                next_num = num + 1
                while next_num in s:
                    current_len += 1
                    next_num += 1
                max_len = max(max_len, current_len)
        return max_len