class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        s = []
        o = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(float(x) / y)
        }

        for t in tokens:
            if t not in o:
                s.append(int(t))
            else:
                y, x = s.pop(), s.pop()
                s.append(o[t](x, y))

        return s[0]
