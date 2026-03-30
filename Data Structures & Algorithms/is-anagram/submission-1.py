class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # compare s and t len
        # make a dict
        # iterate thru s and count each char occur
        # iterate thru t and count each char occur
        # iterate thru s dict and t dict and compare each char occur
        # if anything is uneq return false
        # else true
        if len(s) != len(t):
            return False

        s_dict, t_dict = {}, {}

        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1

        for char in t:
            if char not in t_dict:
               t_dict[char] = 1
            else:
                t_dict[char] += 1
        
        # iterate thru each key, value pair in s dict
        # check that value in s_dict is eq to t_dict value

        # for s_letter in s_dict.keys():
        #     s_count = s_dict[s_letter]
        #     if s_letter not in t_dict:
        #         return False
        #     if t_dict[s_letter] != s_count:
        #         return False
        # return True
    
        return s_dict == t_dict
