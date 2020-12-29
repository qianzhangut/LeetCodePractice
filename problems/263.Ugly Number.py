## check if multiple of 2,3,5, if yes divided by 2, 3, 5, else return false

class Solution:
    def isUgly(self, num: int) -> bool:
        while num>1:
            if num%2 == 0:
                num = num // 2
            elif num%3 == 0:
                num //= 3
            elif num%5 == 0:
                num //= 5
            else:
                return False
                break
        return num == 1
    
                
## more concise code

for p in 2, 3, 5:
    while num % p == 0 < num:
        num /= p
return num == 1