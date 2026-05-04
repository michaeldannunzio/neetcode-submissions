from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        counter = Counter(nums)
        most_common = counter.most_common(1)[0]
        if most_common[1] > 1:
            return True
        return False
