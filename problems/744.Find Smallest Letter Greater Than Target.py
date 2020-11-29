class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r, n = 0, len(letters), len(letters)
        while (l<r):
            mid = l + (r-l)//2
            if letters[mid]<=target:
                l = mid + 1
            else:
                r = mid
        return letters[l%n]