## brutal force

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        rev = [i[::-1] for i in A]
        for i in range(len(rev)):
            for j in range(len(rev[i])):
                rev[i][j] ^= 1
        return rev