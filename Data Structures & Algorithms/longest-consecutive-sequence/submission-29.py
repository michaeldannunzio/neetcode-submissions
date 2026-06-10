class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = list(sorted(nums))
        print(l)
        max_count = counter = 1
        for i in range(len(l)):
            print(l[i])
            d = l[i] - l[i-1]
            if d == 0:
                continue
            if d > 1:
                counter = 0
            else:
                counter += 1
            max_count = max(max_count, counter)
        return max_count
