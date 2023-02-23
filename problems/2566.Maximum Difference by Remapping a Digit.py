class Solution:
    def minMaxDifference(self, num: int) -> int:
        n = str(num)
        i = 0

        while n[i] == '9' and i < len(n)-1:
            i += 1
        return int(n.replace(n[i], '9')) - int(n.replace(n[0], '0'))
 


