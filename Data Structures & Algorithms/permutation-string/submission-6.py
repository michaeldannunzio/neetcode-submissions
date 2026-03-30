from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        l, r = 0, n1
        c = Counter(s1)
        for i in range(n1, n2+1):
            l, r = i-n1, i
            if c == Counter(s2[l:r]):
                return True
        return False
