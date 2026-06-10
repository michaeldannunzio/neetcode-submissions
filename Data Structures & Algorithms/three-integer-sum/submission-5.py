class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, n-1
            while l < r:
                x, y, z = nums[i], nums[l], nums[r]
                s = x + y + z
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([x,y,z])
                    l += 1
                    r -= 1
                    while l < r and y == nums[l-1]:
                        l += 1
        return res
