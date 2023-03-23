class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mt = zip(*matrix)
        s1, s2 = set(), set()
        for i in matrix:
            s1.add(min(i))
        for j in mt:
            s2.add(max(j))

        return s1&s2