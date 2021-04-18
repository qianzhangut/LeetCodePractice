class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:

        ans = [[x,y] for y in range(C) for x in range(R)]
        ans.sort(key=lambda x: abs(x[0]-r0) + abs(x[1]-c0))
        return ans