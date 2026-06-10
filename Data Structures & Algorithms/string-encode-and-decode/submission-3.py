class Solution:

    delimiter = '<$@$$!>:-)'

    def encode(self, strs: List[str]) -> str:
        return self.delimiter.join(strs)

    def decode(self, s: str) -> List[str]:
        r = s.split(self.delimiter)
        if r[0] == "":
            return []
        return r
