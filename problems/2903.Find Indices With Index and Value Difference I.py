class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(i-j)>=indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]

        return [-1,-1]
        
        
    def findIndices(self, A: List[int], d: int, valueDifference: int) -> List[int]:
        mini = maxi = 0
        for i in range(d, len(A)):
            if A[i - d] < A[mini]: mini = i - d
            if A[i - d] > A[maxi]: maxi = i - d
            if A[i] - A[mini] >= valueDifference: return [mini, i]
            if A[maxi] - A[i] >= valueDifference: return [maxi, i]
        return [-1, -1]