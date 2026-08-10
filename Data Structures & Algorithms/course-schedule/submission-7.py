from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapping = {}
        for req in prerequisites:
            if req[::-1] in prerequisites:
                return False
            if not mapping.get(req[0]):
                mapping[req[0]] = [req[1]]
            else:
                mapping[req[0]].append(req[1])
        
        print(mapping)
        for key in mapping.keys():
            q = deque([key])
            while q:
                item = q.popleft()
                if not mapping.get(item):
                    continue
                for nei in mapping[item]:
                    if nei == key:
                        return False
                    else:
                        q.append(nei)
        return True
            
