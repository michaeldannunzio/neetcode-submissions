class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numsSorted = sorted(nums)

        for i in range(len(numsSorted)):
            if i == len(numsSorted) - 1:
                break
            
            if numsSorted[i+1] - numsSorted[i] > 1:
                break
            
            res += 1
        
        if res == 0:
            res = len(numsSorted)

        return res