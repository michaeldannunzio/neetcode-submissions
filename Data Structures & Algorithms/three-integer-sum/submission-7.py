class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i,v in enumerate(nums):
            if v > 0:
                break
            if i > 0 and v == nums[i-1]:
                continue
            l, r = i+1, n-1
            while l < r:
                s = v + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.append([v,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res
