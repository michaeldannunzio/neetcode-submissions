class Solution:

    delimiter = '<$@$$!>:-)'
    empty = '!!^*^!!'

    def encode(self, strs: List[str]) -> str:
        delimiter = self.delimiter if len(strs) > 0 else self.empty
        e = delimiter.join(strs)
        print("strs:",strs)
        print("e:",e)
        return e

    def decode(self, s: str) -> List[str]:
        d = s.split(self.delimiter)
        print("s:",s)
        print("d:",d)
        if s == '':
            return []
        return d
