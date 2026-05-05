from operator import add, sub, mul, truediv as div

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        ops = { '+': add, '-': sub, '*': mul, '/': div }
        stack = []
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                y, x = stack.pop(), stack.pop()
                res = int(ops[t](x, y))
                stack.append(res)
        return stack[0]
