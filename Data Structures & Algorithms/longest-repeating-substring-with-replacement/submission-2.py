class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = collections.defaultdict(int)
        m = f = 0
        l = r = 0
        while r < len(s):
            c[s[r]] += 1
            f = max(f, c[s[r]])
            while r-l+1-f > k:
                c[s[l]] -= 1
                l += 1
            m = max(m, r-l+1)
            r += 1
        return m
