class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        
        A = list(accumulate(sorted(nums)))
        return [bisect_right(A, q) for q in queries]