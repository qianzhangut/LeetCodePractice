class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:

        S = sum([j for j in A if j%2==0])
        res = []
        for val, idx in queries:
            if A[idx]%2 ==0: S-= A[idx]
            A[idx] += val
            if A[idx]%2 ==0: S+= A[idx]
            res.append(S)         
        return res