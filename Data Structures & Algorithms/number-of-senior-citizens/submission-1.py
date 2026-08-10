class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for detail in details:
            if int(detail[11])*10 + int(detail[12]) > 60:
                res += 1
        return res