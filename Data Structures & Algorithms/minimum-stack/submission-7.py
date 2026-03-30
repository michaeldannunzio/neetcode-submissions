class MinStack:

    def __init__(self):
        self._stack = []
        self._min = math.inf
        # self._prevmin = math.inf
        self._top = None
    
    # @log
    def push(self, val: int) -> None:
        self._stack.append(val)
        self._top = val
        # self._prevmin = self._min
        # self._min = min(self._min, val)
        # self._min = min(self._stack)
        # self._min = min(self._stack)

    # @log
    def pop(self) -> None:
        v = self._stack.pop()
        # print(v, self._min, self._prevmin)
        # self._top = self._stack[-1] if self._stack else None
        # if self._stack and self._min == v:
        #     self._min = self._prevmin
        # self._min = 

    # @log
    def top(self) -> int:
        return self._stack[-1]
        # return self._top
    
    # @log
    def getMin(self) -> int:
        return min(self._stack)

    def log(self, f, *args, **kwargs):
        return f