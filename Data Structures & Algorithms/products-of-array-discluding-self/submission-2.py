class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force solution
        # n = len(nums)
        # res = [0] * n
        # for i in range(n):
        #     prod = 1
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         prod *= nums[j]
        #     res[i] = prod
        # return res

        # we can do better
        # division solution
        prod, zero_count = 1, 0
        res = [0] * len(nums)
        for num in nums:
            if num:
                prod *= num
            else:
                zero_count += 1
        
        if zero_count > 1:
            return res
        
        for i,num in enumerate(nums):
            if zero_count:
                res[i] = 0 if num else prod
            else:
                res[i] = prod // num
        return res
            
        