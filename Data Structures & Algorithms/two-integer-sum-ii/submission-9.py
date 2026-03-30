class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        log = self.logger(numbers)
        n = len(numbers)
        l, r = 0, n-1

        while l < r:
            s = numbers[l] + numbers[r]
            log(l,r)
            if s == target:
                return [l+1,r+1]
            if s > target:
                r -= 1
            else:
                l += 1

    def logger(self, nums):
        def log(l, r):
            print(f'l={l}    r={r}    nums[l]={nums[l]}    nums[r]={nums[r]}')
        return log