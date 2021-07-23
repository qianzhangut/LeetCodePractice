class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        t = text.split(" ")
        cnt = len(t)
        for i in t:
            for j in brokenLetters:
                if j in i:
                    cnt -= 1
                    break
                    
        return cnt
            