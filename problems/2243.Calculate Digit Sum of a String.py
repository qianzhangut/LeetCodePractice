class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            new = [s[i:i+k] for i in range(0,len(s), k)]
            s = ''
            for j in new:
                s += str(sum([int(x) for x in j]))
                
        return s