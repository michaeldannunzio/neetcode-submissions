class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref = min(strs, key=len)
        res = ''
        for i in range(len(ref)):
            for s in strs:
                if s[i] != ref[i]:
                    return res
            res += ref[i]
        return res
