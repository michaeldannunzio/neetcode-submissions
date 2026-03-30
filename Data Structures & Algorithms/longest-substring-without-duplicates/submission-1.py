class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = collections.deque()
        m = 0
        for c in s:
            while c in ss:
                ss.popleft()
            ss.append(c)
            m = max(m, len(ss))
        return m