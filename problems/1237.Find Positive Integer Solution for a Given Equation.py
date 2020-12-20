class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        y = 1000
        res = []
        for x in range(1,1001):
            while y>1 and customfunction.f(x,y) > z:
                y -= 1
            if customfunction.f(x,y) == z:
                res.append([x,y])
        return res