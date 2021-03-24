class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cnt = {'D':0, 'U':0, 'L':0, 'R':0}
    
        for i in moves:
            cnt[i] = cnt.get(i,0)+1
        return cnt['L'] == cnt['R'] and cnt['U'] == cnt['D']