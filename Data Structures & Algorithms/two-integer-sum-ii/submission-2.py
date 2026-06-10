class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n-1

        if n == 2:
            return [0,1]

        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l,r]
            if s > target:
                r -= 1
            else:
                l += 1
