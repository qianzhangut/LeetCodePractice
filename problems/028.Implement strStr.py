class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '': return 0
        nlen, hlen = len(needle), len(haystack)
        for i in range(hlen-nlen+1):
            if haystack[i:i+nlen] ==needle:
                return i
        return -1
        