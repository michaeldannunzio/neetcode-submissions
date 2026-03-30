class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        ps = [(p,s) for p,s in zip(position,speed)]
        ps.sort(reverse=True)
        ss = []
        for p,s in ps:
            ss.append((target - p) / s)
            if len(ss) >= 2 and ss[-1] <= ss[-2]:
                ss.pop()
        return len(ss)
