

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr: list(tuple(int,int)) = [(num,i) for i,num in enumerate(sorted(nums))]
        l = 0
        r = len(nums) - 1

        while l < r:
            if arr[l][0] + arr[r][0] == target:
                return [arr[l][1], arr[r][1]]
            if arr[l][0] + arr[r][0] > target:
                r -= 1
            else:
                l += 1
