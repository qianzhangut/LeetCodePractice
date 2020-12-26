## count each bit ==1

class Solution:
    def countBits(self, num: int) -> List[int]:    
        def getone( a):
            cnt = 0
            while a>0:
                if a%2 == 1:
                    cnt += 1
                a=a//2
            return cnt
        res = []
        for i in range(num+1):
            res.append(getone(i))
        return res
