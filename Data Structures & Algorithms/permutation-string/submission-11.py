from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        counter1, counter2 = Counter(s1), Counter(s2[0:n1])
        if counter1 == counter2:
            return True
        for i in range(n1, n2):
            l, r = i-n1, i
            counter2[s2[l]] -= 1
            counter2[s2[r]] += 1
            if counter1 == counter2:
                return True
        return False
