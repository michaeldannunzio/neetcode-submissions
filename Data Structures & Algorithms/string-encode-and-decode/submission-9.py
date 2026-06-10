class Solution:

    delimiter = '<$@$$!>:-)'

    def encode(self, strs: List[str]) -> str:
        e = self.delimiter.join(strs)
        print("strs:",strs)
        print("e:",e)
        return e

    def decode(self, s: str) -> List[str]:
        d = s.split(self.delimiter)
        print("s:",s)
        print("d:",d)
        return d
