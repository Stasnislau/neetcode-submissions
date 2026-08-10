class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
        res = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while carry or i >= 0:
            first = 0 if i < 0 else int(a[i])
            second = 0 if j < 0 else int(b[j])
            val = (carry + first + second )
            if val > 1:
                carry = 1
            else:
                carry = 0
            res.append(str(val % 2))
            i -= 1
            j -= 1
        print(res)
        return "".join(res[::-1])