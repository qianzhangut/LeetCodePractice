## brutal force
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            if i%3 == 0 and i%5 == 0:
                res.append('FizzBuzz')
            elif i%5 == 0:
                res.append('Buzz')
            elif i%3==0:
                res.append('Fizz')
            else:
                res.append(str(i))
        return res
        
## use true and false. True and False are subclass of int, true = 1, false = 0
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ['Fizz'*(i%3==0) + 'Buzz'*(i%5==0) or str(i) for i in range(1,n+1)]