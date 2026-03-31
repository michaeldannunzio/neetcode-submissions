from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.keystore = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keystore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        values = self.keystore[key]
        l, r = 0, len(values) - 1
        while l <= r:
            i = (l + r) // 2
            stored_v, stored_ts = values[i]
            if stored_ts <= timestamp:
                res = stored_v
                l = i + 1
            else:
                r = i - 1
        return res