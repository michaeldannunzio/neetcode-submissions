class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s, r = [], [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while s and t > s[-1][0]:
                pt, pi = s.pop()
                r[pi] = i - pi
            s.append((t, i))
        return r