class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res, index = math.inf, -1
        for i, (l, r) in enumerate(points):
            if (x-l)*(y-r) == 0 and abs(x-l) + abs(y-r)<res:
                res = abs(x-l) + abs(y-r)
                index = i
        return index
            
        
        