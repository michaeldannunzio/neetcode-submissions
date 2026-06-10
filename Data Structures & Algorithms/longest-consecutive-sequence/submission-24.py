class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = list(sorted(nums))
        print(l)
        counter = 1
        for i in range(len(l)):
            print(l[i])
            d = l[i] - l[i-1]
            if d == 0:
                continue
            if d > 1:
                counter = 0
            counter += 1
        
        return counter
            