class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        s = []
        ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(float(x) / y)
        }

        for t in tokens:
            if t not in ops:
                s.append(int(t))
            else:
                y, x = s.pop(), s.pop()
                s.append(ops[t](x, y))

        return s[0]
