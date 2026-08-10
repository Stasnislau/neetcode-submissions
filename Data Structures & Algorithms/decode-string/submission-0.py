class Solution:
    def decodeString(self, s: str) -> str:
        curr_num = 0
        stack = []
        res = ''
        curr_str = ''
        for c in s:
            if '0' <= c <= '9':
                curr_num = curr_num * 10 + int(c)
            elif c == '[':
                stack.append([curr_num, curr_str])
                curr_str = ''
                curr_num = 0
            elif c == ']':
                num, curr = stack.pop()
                if not stack:
                    res += curr+ curr_str * num
                    curr_str = ''
                else:
                    curr_str =curr + curr_str * num 
            else:
                curr_str += c
        res += curr_str
        return res