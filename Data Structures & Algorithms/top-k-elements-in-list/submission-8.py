from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        most_common = Counter(nums).most_common(k)
        return [v for v,_ in most_common]