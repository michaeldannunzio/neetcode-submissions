from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = deque()
        max_len = 0
        for c in s:
            while c in queue:
                queue.popleft()
            queue.append(c)
            max_len = max(max_len, len(queue))
        return max_len
