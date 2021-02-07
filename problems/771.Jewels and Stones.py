
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
         
        for item in stones:
            if item in jewels:
                cnt +=1
        return cnt