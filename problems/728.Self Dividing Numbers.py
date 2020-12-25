class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
            for ch in list(str(i)):
                if ch == '0' or i%int(ch) > 0:
                    break
            else:
                res.append(i)
            
        return res
            