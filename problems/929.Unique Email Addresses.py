class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for item in emails:
            local, domain = item.split('@')
            for i in range(len(local)):
                if '+' in local:
                    local = local[:local.index('+')]
            local = local.replace('.', '')        
            ans.add(local+'@'+domain)


        return len(ans)