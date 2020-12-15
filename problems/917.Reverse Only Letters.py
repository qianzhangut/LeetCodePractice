
## double pointer
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        xs = list(S)
        j = len(S)-1
        for c in S:
            if c.isalpha():
                while not xs[j].isalpha():
                    j -= 1   
                xs[j] = c
                j -= 1
        return ''.join(xs)