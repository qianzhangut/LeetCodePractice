##brutal force
class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        
        for i in range(1,num+1):
            res = 0
            while i>0:
                res += i%10
                i=i//10
            if res%2 ==0:
                ans += 1
                
        return ans
        
#map
class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        for i in range(1, num+1):
            if sum(map(int, str(i))) %2 ==0 :
                ans += 1
        return ans
        
        
        
#odd even rulle
class Solution:
    def countEven(self, num: int) -> int:
        return (num - 1) // 2 if sum(map(int, str(num))) % 2 else num // 2