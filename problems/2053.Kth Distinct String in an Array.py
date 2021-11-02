class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}
        for i in arr:
            d[i] = d.get(i, 0 ) + 1
            
            
        res = [j for j in d if d[j]==1]
        
        return res[k-1] if k-1<len(res) else ""