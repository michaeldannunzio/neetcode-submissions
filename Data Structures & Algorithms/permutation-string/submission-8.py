from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        c1, c2 = Counter(s1), Counter(s2[0:n1])
        for i in range(n1, n2+1):
            l, r = i-n1, i
            # c2.update(**{k: v})   # how to update c2 ?
            c2[s2[l]] -= 1
            c2[s2[r-1]] += 1
            if c1 == c2:
                return True
        return False
