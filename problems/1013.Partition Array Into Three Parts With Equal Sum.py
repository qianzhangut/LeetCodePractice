class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        avg, div, cnt, part = sum(arr)//3, sum(arr)%3, 0, 0 
        
        for i in arr:
            part += i
            if part == avg:
                cnt += 1
                part = 0
                
        return not div and cnt>=3