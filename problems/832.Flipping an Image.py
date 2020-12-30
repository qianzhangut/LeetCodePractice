## brutal force

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        rev = [i[::-1] for i in A]
        for i in range(len(rev)):
            for j in range(len(rev[i])):
                rev[i][j] ^= 1
        return rev
        
## list comprehension one line

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[i^1 for i in row[::-1]] for row in A]