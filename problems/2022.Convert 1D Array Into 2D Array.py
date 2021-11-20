class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        k, i = 0, 0
        if len(original) != m*n:
            return []
        else:
            while k<m:
                ans.append(original[i:i+n])
                i += n
                k+=1
            return ans