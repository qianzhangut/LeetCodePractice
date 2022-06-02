class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = -1
        
        for i in range(len(num)-2):
            if len(set(list(num[i:i+3])))==1:
                ans = max(ans, int(num[i:i+3]))
       
            
        if ans ==0 :
            return "000"
        elif ans > 0 :
            return str(ans)
        else:
            return ""