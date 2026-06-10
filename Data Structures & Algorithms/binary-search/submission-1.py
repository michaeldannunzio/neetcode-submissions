class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        i = (r - l) // 2
        print(i)
        while l < r:
            i = (r - l) // 2
            print(i)
            v = nums[i]
            if v == target:
                return i
            elif v > target:
                r = i
            else:
                l = i
        return -1
