# 1. use sort

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# 2. use hash

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dict_s = {}
        for i in s:
            if i not in dict_s:
                dict_s[i] =0
            dict_s[i] +=1

        for j in t:
            if j not in dict_s:
                return False
            dict_s[j] -= 1
            if dict_s[j]<0:
                return False

        for k,v in dict_s.items():
            if v != 0:
                return False
        return True
