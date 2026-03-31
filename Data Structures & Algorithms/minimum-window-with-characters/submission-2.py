from collections import Counter
import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t):
            return ''
        
        t_counter = Counter(t)
        s_counter = Counter(s[0:len(t)])

        if t_counter <= s_counter:
            return s[0:len(t)]

        res = [0, 0]
        res_len = math.inf
        l = 0
        
        for r in range(len(t), len(s)):
            s_counter.update(s[r])
            while t_counter <= s_counter:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                s_counter.subtract(s[l])
                l += 1

        l, r = res
        return s[l:r+1] if res_len != math.inf else ''
