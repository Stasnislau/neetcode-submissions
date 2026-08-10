class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        j = 0
        paths = path.split('/')
        print(paths)
        for p in paths:
            if p == '..':
                if stack:
                    stack.pop()
                continue
            if p and p != '.':
                stack.append(p)
        return '/' + '/'.join(stack)




            
        