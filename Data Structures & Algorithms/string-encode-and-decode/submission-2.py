class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        number = ''
        strs = []
        i = 0
        while i < len(s):
            if s[i] != '#':
                number += s[i]
                i += 1
            else:
                i += 1
                j = i;
                i += (int(number))
                number = ''
                strs.append(s[j:i])
        return strs        