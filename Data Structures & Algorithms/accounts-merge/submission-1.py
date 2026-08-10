class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parents = {}
        rank = {}
        for account in accounts:
            for i in range(1,len(account)):
                parents[account[i]] = account[i]
                rank[account[i]] = 1
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        def union(x,y):
            par_x = find(x)
            par_y = find(y)
            if par_y == par_x:
                return False
            if rank[par_x] > rank[par_y]:
                rank[par_x] += rank[par_y]
                parents[par_y] = par_x
            else:
                rank[par_y] += rank[par_x]
                parents[par_x] = par_y
            return True
        res = []
        for account in accounts:
            for i in range(1, len(account)):
                union(account[i], account[1])
        email_to_name = {}
        for account in accounts:
            for i in range(1, len(account)):
                email_to_name[account[i]] = account[0]
        # группируй по root
        groups = defaultdict(list)
        for email in parents:
            root = find(email)
            groups[root].append(email)
        # собери ответ
        res = []
        for root, emails in groups.items():
            res.append([email_to_name[root]] + sorted(emails))
        return res
        