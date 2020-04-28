class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        j,l =0,0
        for i in range(len(s)):
            j = max(j, d.get(s[i],-1)+1)
            l = max(l,i-j+1)
            d[s[i]]=i
        return l
            
        