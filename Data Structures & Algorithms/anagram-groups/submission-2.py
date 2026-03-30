from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r: dict[str, list[str]] = defaultdict(list)
        for s in strs:
            l = list(s)
            l.sort()
            r[''.join(l)].append(s)
        return list(r.values())
