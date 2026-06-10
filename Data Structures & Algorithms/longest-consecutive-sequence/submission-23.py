class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = list(sorted(nums))
        print(l)
        counter = 1
        for i in range(len(l)):
            print(l[i])
            if l[i] - l[i-1] > 1:
                counter = 0
            
            counter += 1
        
        return counter
            