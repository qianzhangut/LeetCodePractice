class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        for i in range(1, len(A)):
            A[i] += A[i - 1] * 2
        return [x % 5 == 0 for x in A]
        
# bit operation
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        ans, b = [], 0
        for a in A:
            b = b << 1 | a
            ans.append(b % 5 == 0)
        return ans