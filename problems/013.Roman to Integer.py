class Solution:
    def romanToInt(self, s: str) -> int:
          lookup = {
            'M': 1000, 
            'D': 500, 
            'C': 100, 
            'L': 50, 
            'X': 10, 
            'V': 5, 
            'I': 1
          }
          ans, t,p=0,0,0
          for i in range(len(s)):
            ans+=lookup[s[i]]
            if lookup[s[i]]>lookup[s[p]]:
              t+=-2*lookup[s[p]]
            p=i
          return ans+t