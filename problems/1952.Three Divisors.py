class Solution:
    def isThree(self, n: int) -> bool:
        cnt = 0
        for i in range(2, n):
            if n%i ==0:
                cnt +=1
                if cnt > 1:
                    return False
        return cnt == 1