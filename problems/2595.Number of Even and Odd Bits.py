class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ans = bin(n)[2:][::-1]

        od, ev = 0, 0
        for i in range(len(ans)):

            if i%2==1 and ans[i]=='1':
                od +=1
            if i%2==0 and ans[i]=='1':
                ev +=1
        return [ev, od]