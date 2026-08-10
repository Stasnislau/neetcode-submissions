class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        j = 0
        while j < len(path):
            while j < len(path) and path[j] == '/':
                j += 1
                i += 1
            while j < len(path) and path[j] == '.':
                j += 1
            if j - i == 1 and (j == len(path) or path[j] == '/'):
                i += 1
            elif j - i == 2 and (j == len(path) or path[j] == '/'):
                if stack:
                    stack.pop()
                i = j
            
            while j < len(path) and path[j] != '/':
                j += 1
            if i != j:
                stack.append(path[i:j])
            i = j
        print(stack)
        return '/' + "/".join(stack)




            
        