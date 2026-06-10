class Solution:

    delimiter = '<$@$$!>:-)'

    def encode(self, strs: List[str]) -> str:
        return self.delimiter.join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split(self.delimiter)
