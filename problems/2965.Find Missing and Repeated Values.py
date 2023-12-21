class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        temp = [i for j in grid for i in j]
        d = {}
        for x in temp:
            d[x] = d.get(x,0) +1
            if d[x]==2:
                a = x

        b = [y for y in set(range(1,len(temp)+1)) if y not in set(temp)][0]

        return [a,b]