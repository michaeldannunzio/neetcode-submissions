class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs = [(p,s) for p,s in zip(position,speed)]
        pairs.sort(reverse=True)
        stack = []
        for pos, s in pairs:
            stack.append((target - pos) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
