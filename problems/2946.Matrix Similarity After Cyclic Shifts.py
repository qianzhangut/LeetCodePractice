class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        nmat = []
        k = k%len(mat[0])
        for i in range(len(mat)):

                nmat = [mat[i][k:] + mat[i][:k] for i in mat]
                

        return mat == nmat
        