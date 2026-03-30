from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # solution 1
        # return sorted(s) == sorted(t)

        # solution 2
        return Counter(s) == Counter(t)
