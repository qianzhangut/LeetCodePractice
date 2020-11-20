class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d = {}
        for item in arr:
            if item not in d:
                d[item] = 1 
            else:
                d[item] += 1
            if d[item]/len(arr)>0.25:
                return item