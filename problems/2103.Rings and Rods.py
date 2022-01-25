## burtalforce

class Solution:
    def countPoints(self, rings: str) -> int:
        d = {f"{i}":[] for i in range(10)}
        res = 0
        for i in range(1,len(rings),2):
            d[rings[i]].append(rings[i-1])

        for i in range(10):
            if len(set(d[str(i)]))== 3:
                res += 1
        return res
            