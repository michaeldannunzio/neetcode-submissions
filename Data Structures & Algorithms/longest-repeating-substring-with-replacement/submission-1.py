class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.defaultdict(int)
        m = f = 0
        l = r = 0
        while r < len(s):
            count[s[r]] += 1
            f = max(f, count[s[r]])
            while r-l+1-f > k:
                count[s[l]] -= 1
                l += 1
            m = max(m, r-l+1)
            r += 1
        return m
