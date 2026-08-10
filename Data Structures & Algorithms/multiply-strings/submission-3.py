class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        if num1 == '0' or num2 == '0':
            return '0'
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        for ind in range(len(num2) - 1, -1, -1):
            base = num2[ind]
            prelim_res = 0
            for i in range(len(num1) - 1, -1, -1):
                num = num1[i]
                curr_res = (int(num) * int(base)) * 10**(len(num1) -i - 1)
                print(curr_res, 'curr')
                prelim_res += curr_res
            prelim_res *= 10**(len(num2)- ind - 1)
            print(prelim_res)
            res += prelim_res
        return str(res)