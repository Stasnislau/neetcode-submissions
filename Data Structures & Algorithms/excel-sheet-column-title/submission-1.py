class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            diff = columnNumber % 26
            res.append(chr(ord('A') + diff))
            columnNumber = columnNumber // 26
        return ''.join(res[::-1])