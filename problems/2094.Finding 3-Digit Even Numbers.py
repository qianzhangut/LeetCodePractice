## counter +/-wsl

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        from collections import Counter
        ans =[]
        
        freq = Counter(digits)


        for x in range(100, 1000, 2): 
            if not Counter(int(d) for d in str(x)) - freq: 
                ans.append(x)
                
        return ans
        
        
## brutal force
def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = set()
        for x, y, z in permutations(digits, 3): 
            if x != 0 and z & 1 == 0: 
                ans.add(100*x + 10*y + z) 
        return sorted(ans)