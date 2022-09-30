class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = {i:j for i, j in zip(heights, names)}
        
        hh = sorted(heights,reverse=True)
        
        return [d[k] for k in hh]
        