class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cnt = {'D':0, 'U':0, 'L':0, 'R':0}
    
        for i in moves:
            cnt[i] = cnt.get(i,0)+1
        return cnt['L'] == cnt['R'] and cnt['U'] == cnt['D']
        
        
#use coordinate

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for move in moves:
            if move == 'U': y -= 1
            elif move == 'D': y += 1
            elif move == 'L': x -= 1
            elif move == 'R': x += 1

        return x == y == 0
 