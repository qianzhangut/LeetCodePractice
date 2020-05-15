class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [1 for i in range(n)]

        i = 2
        while i * i < n:
        	if isPrime[i]:
        		j = i * i 
        		while j < n :
        			isPrime[j] = 0
        			j += i
        	i += 1

        return sum(isPrime[2:])