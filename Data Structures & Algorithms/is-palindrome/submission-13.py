class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alnum = [c.lower() for c in s if c.isalnum()]
        n = len(s_alnum)
        l, r = 0, n-1

        while l <= r:
            if s_alnum[l] != s_alnum[r]:
                return False
            l += 1
            r -= 1
        return True
