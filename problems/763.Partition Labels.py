## set
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
        
        
## two pointer O(n)
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        rightmost = {c:i for i, c in enumerate(S)}
        left = right = 0
        ans = []
        for i, c in enumerate(S):
            right = max(right, rightmost[c])
            
            if i == right:
                ans.append(right - left +1)
                left = i + 1 
                
        return ans