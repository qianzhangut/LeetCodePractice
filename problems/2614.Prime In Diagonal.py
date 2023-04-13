class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        ans = 0
        def is_prime(n):
        # If n is less than 2, it is not prime
            if n < 2:
                return False
            # Loop from 2 to the square root of n
            for i in range(2, int(n ** 0.5) + 1):
                # If n is divisible by i, it is not prime
                if n % i == 0:
                    return False
            # If no divisor is found, it is prime
            return True

        for i in range(len(nums)):
            ans = max(ans, is_prime(nums[i][i])*nums[i][i], is_prime(nums[i][len(nums)- i - 1])*nums[i][len(nums)- i - 1])


        return ans 