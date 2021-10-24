class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        
        ans = [int(i) for i in s.split(" ") if i.isdigit()]
        return all(ans[j]<ans[j+1] for j in range(len(ans)-1))
 #walnut expression 
            
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = 0
        for token in s.split():
            if token.isnumeric():                
                if (curr := int(token)) <= prev:
                    return False
                prev = curr
        return True