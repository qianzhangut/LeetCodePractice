class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        ctr = Counter(moves)

        return abs(ctr['L'] - ctr['R']) + ctr['_']