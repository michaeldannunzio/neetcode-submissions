from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        most_common = counter.most_common(1)[0]
        if most_common[1] > 1:
            return True
        return False
