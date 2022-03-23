class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7': "pqrs", 
        '8':"tuv", '9':"wxyz"}

        ans = [''] if digits else []
        for d in digits:
            ans = [p + q for p in ans for q in dict[d]]
            
        return ans