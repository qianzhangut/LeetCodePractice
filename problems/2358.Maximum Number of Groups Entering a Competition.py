class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        return (int)(sqrt(len(grades) * 2 + 0.25) - 0.5)
