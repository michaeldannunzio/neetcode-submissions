class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict: dict[str, List[str]] = {}
        # res: List[List[str]] = []
        # strs.sort(key=len)

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in anagramDict:
                anagramDict[sorted_s] = []
            anagramDict[sorted_s].append(s)
        
        # print(list(anagramDict.values()))

        return list(anagramDict.values())

        # if len(res) == 0:
        #     res.append([""])
        
        # return res



    def areAnagrams(self, str1: str, str2: str) -> bool:
        return sorted(str1) == sorted(str2)
