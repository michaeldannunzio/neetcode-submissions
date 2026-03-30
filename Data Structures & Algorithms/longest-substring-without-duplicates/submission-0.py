class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = collections.deque()
        max_len = 0
        for c in s:
            while c in substr:
                substr.popleft()
            substr.append(c)
            max_len = max(max_len, len(substr))
        return max_len
