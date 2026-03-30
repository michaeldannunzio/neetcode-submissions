class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    prods[i] *= nums[j]

        return prods
