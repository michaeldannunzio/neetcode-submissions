class Solution:
    def isValid(self, s: str) -> bool:
        bm = {')':'(', ']':'[', '}':'{'}
        if len(s) % 2 or s[0] in bm:
            return False
        x = []
        for b in s:
            if b not in bm:
                x.append(b)
            elif x and x[-1] == bm[b]:
                x.pop()
            else:
                return False
        return False if x else True
