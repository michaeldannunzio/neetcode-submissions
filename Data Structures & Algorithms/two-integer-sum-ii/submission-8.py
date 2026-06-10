class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        log = self.logger(numbers)
        n = len(numbers)
        l, r = 0, n-1

        while l < r:
            s = numbers[l] + numbers[r]
            log(l,r)
            if s == target:
                return [numbers[l],numbers[r]]
            if s < target:
                l += 1
            else:
                r -= 1

    def logger(self, nums):
        def log(l, r):
            print(f'l={l}    r={r}    nums[l]={nums[l]}    nums[r]={nums[r]}')
        return log