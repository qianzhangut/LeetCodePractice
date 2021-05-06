class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ans = []
        
        while S:
            i = 1
            while set(S[:i]) & set(S[i:]):
                i += 1
            ans.append(i)
            S = S[i:]
        return ans