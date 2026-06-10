class MinStack:

    def __init__(self):
        self._stack = []
        self._min = math.inf
        self._prevmin = math.inf
        self._top = None
    
    # @log
    def push(self, val: int) -> None:
        self._stack.append(val)
        self._top = val
        self._prevmin = self._min
        self._min = min(self._min, val)

    # @log
    def pop(self) -> None:
        v = self._stack.pop()
        self._top = self._stack[-1] if self._stack else None
        if self._stack and self._min == v:
            self._min = self._prevmin

    # @log
    def top(self) -> int:
        return self._top
    
    # @log
    def getMin(self) -> int:
        return self._min

    def log(self, f, *args, **kwargs):
        return f