class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        res = 1
        nums = sorted(nums)

        for i in range(len(nums)):
            if i == len(nums) - 1:
                if i == 0:
                    res += 1
                break
            # print(f"{nums[i+1]} - {nums[i]} = {nums[i+1] - nums[i]}")
            if nums[i+1] - nums[i] > 1:
                break
            res += 1
        
        return res
        
        # numsSorted = sorted(nums)
        # for i in range(len(numsSorted)):
        #     if i == len(numsSorted) - 1:
        #         break
        #     if numsSorted[i+1] - numsSorted[i] > 1:
        #         break
        #     res += 1
        # if res == 0:
        #     res = len(numsSorted)
        # return res