class Solution:
    def reverse(self, x: int) -> int:
        min_val, max_val = -2**31, 2**31-1
        sig=-1 if x<0 else 1
        x=abs(x)
        ans=0
        while x!=0:
            ans = ans*10 + (x%10)
            x=x//10
        if ans>=max_val or ans<min_val: return 0
        return ans*sig