class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            result += f'{len(s)}#{s}'
        return result

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