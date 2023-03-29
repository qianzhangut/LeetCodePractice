class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = [1]*numOnes + [0]*numZeros + [-1]*numNegOnes
        return sum(ans[:k])
        
#one liner
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        return min(k, numOnes) - max(0, k - numZeros - numOnes)