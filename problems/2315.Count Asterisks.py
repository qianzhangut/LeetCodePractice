class Solution:
    def countAsterisks(self, s: str) -> int:
        cnt , bar = 0, True
        
        for i in s:
            if i =='|':
                bar = not bar
            if i == '*' and bar:
                cnt += 1
                
        return cnt