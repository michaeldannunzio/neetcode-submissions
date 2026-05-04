from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        k_most_common = counter.most_common(k)
        return [num for num, count in k_most_common]
