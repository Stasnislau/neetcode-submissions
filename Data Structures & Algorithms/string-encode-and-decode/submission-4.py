class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        number = ''
        strs = []
        start = 0
        end = 0
        while end < len(s):
            end = s.find('#', start)
            num = int(s[start:end])
            start = end + 1
            end = start + num
            strs.append(s[start:end])
            start = end

        return strs        