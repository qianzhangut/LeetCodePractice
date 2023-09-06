class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0

        for i in range(low, high+1):
            l = [int(x) for x in list(str(i))]
            if sum(l[:len(l)//2])==sum(l[len(l)//2:]) and  len(l)%2==0:
                ans +=1

        return ans
        