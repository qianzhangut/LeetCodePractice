class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = s + fill * (k-len(s)%k) if len(s)%k != 0 else s
        
        return [res[i:i+k] for i in range(0,len(res),k)]