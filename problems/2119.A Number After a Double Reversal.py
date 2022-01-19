class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == int(str(int(str(num)[::-1]))[::-1])
        
        
##  0 or end digit is 0
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return (num == 0) | (num % 10)