
### flat the list

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums)*len(nums[0]) != r*c:
            return nums
        new = [j for i in nums for j in i]
        
        res = []
        for i in range(0, len(new), c):
            res.append(new[i:i+c]) 
        return res