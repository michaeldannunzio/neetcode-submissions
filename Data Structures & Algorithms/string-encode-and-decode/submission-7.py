class Solution:

    delimiter = '<$@$$!>:-)'

    def encode(self, strs: List[str]) -> str:
        print(strs)
        return self.delimiter.join(strs)

    def decode(self, s: str) -> List[str]:
        print(s)
        return s.split(self.delimiter)
