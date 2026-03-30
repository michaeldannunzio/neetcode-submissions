class Solution:

    delimiter = '<$@$$!>:-)'
    empty = '!!^*^!!'

    def encode(self, strs: List[str]) -> str:
        return self.delimiter.join(strs) if len(strs) > 0 else self.empty

    def decode(self, s: str) -> List[str]:
        return s.split(self.delimiter) if s != self.empty else []
