from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        make_counter = lambda s: Counter(s, **{chr(n): 0 for n in range(ord('a'), ord('z') + 1)})
        l, r = 0, n1
        c1, c2 = make_counter(s1), make_counter(s2[l:r])
        for i in range(n1, n2+1):
            l, r = i-n1, i
            c2 = make_counter(s2[l:r])
            if c1 == c2:
                return True
        return c1 == c2
