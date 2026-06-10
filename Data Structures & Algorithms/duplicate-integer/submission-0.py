class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}

        for num in nums:
            if d[num] is not None:
                #d[num] += 1
                return True
            else:
                d[num] = 1

        return False
