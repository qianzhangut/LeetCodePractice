class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        
        ans = [int(i) for i in s.split(" ") if i.isdigit()]
        return all(ans[j]<ans[j+1] for j in range(len(ans)-1))
            