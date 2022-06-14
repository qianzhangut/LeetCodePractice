class Solution:
    def digitCount(self, num: str) -> bool:
        d = {}
        for i in num:
            d[i] = d.get(i, 0) + 1
            
        return all( int(num[j])==d.get(str(j),0) for j in range(len(num)))