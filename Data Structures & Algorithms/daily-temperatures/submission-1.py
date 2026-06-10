class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, res = [], [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prev_t, prev_i = stack.pop()
                res[prev_i] = i - prev_i
            stack.append((temp, i))
        return res
