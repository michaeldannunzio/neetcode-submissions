from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_map = defaultdict(list)
        for s in strs:
            res_map[''.join(sorted(list(s)))].append(s)
        return list(res_map.values())
