class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = { ')': '(', '}': '{', ']': '[' }
        
        if s[0] in bracket_map \
        or s[-1] in bracket_map.values() \
        or len(s) % 2 != 0:
            return False

        stack = []
        for bracket in s:
            if bracket not in bracket_map:
                stack.append(bracket)
            elif stack and stack[-1] == bracket_map[bracket]:
                stack.pop()
            else:
                return False
        return False if stack else True
