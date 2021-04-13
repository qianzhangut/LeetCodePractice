class Solution:
    def wordSubsets(self, A, B):
        cnt = Counter()
        for b in B:
            cnt |= Counter(b)
            
        return [a for a in A if not cnt - Counter(a)]