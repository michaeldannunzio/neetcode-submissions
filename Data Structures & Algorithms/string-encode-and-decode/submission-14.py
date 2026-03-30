class Solution:

    delimiter = '<$@$$!>:-)'
    empty = '!!^*^!!'

    def encode(self, strs: List[str]) -> str:
        # delimiter = self.delimiter if len(strs) > 0 else self.empty
        if len(strs) == 0:
            return self.empty
        e = self.delimiter.join(strs)
        print("strs:",strs)
        print("e:",e)
        return e 

    def decode(self, s: str) -> List[str]:
        if s == self.empty:
            return []
        d = s.split(self.delimiter)
        print("s:",s)
        print("d:",d)
        return d
