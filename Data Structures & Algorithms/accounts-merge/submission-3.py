from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}
        parents = {}
        sizes = {} 
        for account in accounts:
            for i in range(1, len(account)):
                parents[account[i]] = account[i]
                sizes[account[i]] = 1
                email_to_name[account[i]] = account[0]
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x]) 
            return parents[x]
        def union(x,y):
            par_x = find(x)
            par_y = find(y)
            if par_x == par_y:
                return False
            if sizes[par_x] > sizes[par_y]:
                sizes[par_x] += sizes[par_y]
                parents[par_y] = par_x
            else:
                sizes[par_y] += sizes[par_x]
                parents[par_x] = par_y
            return True
        for account in accounts:
            for i in range(1, len(account)):
                union(account[i], account[1])
        groups = defaultdict(list)
        for email in email_to_name:
            groups[find(email)].append(email)
        res = []
        for group, emails in groups.items():
            res.append([email_to_name[group]] + sorted(emails))
        return res

        