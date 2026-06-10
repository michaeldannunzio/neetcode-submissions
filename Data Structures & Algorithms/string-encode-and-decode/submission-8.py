class Solution:

    delimiter = '<$@$$!>:-)'

    def encode(self, strs: List[str]) -> str:
        r = self.delimiter.join(strs)
        print(strs)
        print(r)
        return r

    def decode(self, s: str) -> List[str]:
        r = s.split(self.delimiter)
        print(s)
        print(r)
        return r
