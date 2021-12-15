class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        from collections import Counter
        ans =[]
        
        freq = Counter(digits)


        for x in range(100, 1000, 2): 
            if not Counter(int(d) for d in str(x)) - freq: 
                ans.append(x)
                
        return ans