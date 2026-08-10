class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        checked = set()
        for email in emails:
            curr = []
            local, domain = email.split('@')
            for c in local:
                if c == '+':
                    break
                if c == '.':
                    continue
                curr.append(c)
            checked.add("".join(curr) + '@' + domain)
        return len(checked)