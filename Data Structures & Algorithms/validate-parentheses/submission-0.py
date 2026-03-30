class Solution:
    def isValid(self, s: str) -> bool:
        bm = {')':'(', ']':'[', '}':'{'}
        if len(s) % 2 or s[0] in bm:
            return False
        x = []
        for b in s:
            if b in bm:
                if x and x[-1] == bm[b]:
                    x.pop()
                else:
                    return False
            else:
                x.append(b)
        return False if x else True
