class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        p, ans = 0, ''
        for i in range(len(s))[::-1]:
            p += shifts[i]
            if (ord(s[i]) + p%26) > ord('z'):
                ans += chr(ord(s[i]) + p%26 - ord('z') + ord('a')-1)
            else:
                ans += chr(ord(s[i]) + p%26)
        return ans[::-1]