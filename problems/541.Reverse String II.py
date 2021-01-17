class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = list(s)
        for i in range(0,len(s),2*k):
            l[i:i+k] = l[i:i+k][::-1]
            
        return ''.join(l)
        