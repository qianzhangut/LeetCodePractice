class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def get_d(x,y):
            return (x[0]-y[0])**2+(x[1]-y[1])**2
        
        
        ans = [get_d(p1,p2),get_d(p2,p3),get_d(p3,p4),get_d(p1,p4),get_d(p1,p3),get_d(p2,p4)]
        
        d ={}
        for i in ans:
            d[i] = d.get(i, 0) + 1
            
        return len(d)==2 and 2 in d.values() and 4 in d.values() and 0 not in d.keys()