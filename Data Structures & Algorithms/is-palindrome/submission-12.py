class Solution:
    def isPalindrome(self, s: str) -> bool:
        ps = [c.lower() for c in s if c.isalnum()]
        n = len(ps)
        l, r = 0, n-1

        while l <= r:
            if ps[l] != ps[r]:
                return False
            l += 1
            r -= 1
        return True