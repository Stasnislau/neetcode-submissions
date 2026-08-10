class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            res.append([1])
            prev = None
            if len(res) > 1:
                prev = res[-2]
            arr = res[-1]
            for j in range(1, len(prev)):
                arr.append(prev[j]+prev[j-1])
            arr.append(1)
        return res