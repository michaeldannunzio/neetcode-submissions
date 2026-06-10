class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numsSorted = sorted(nums)

        print(numsSorted)

        for i in range(len(numsSorted)):
            if i == len(numsSorted) - 1:
                break
            
            if numsSorted[i+1] - numsSorted[i] > 1:
                break
            
            res += 1
            
        return res