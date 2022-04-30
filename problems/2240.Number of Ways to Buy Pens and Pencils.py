class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        count, max_val = 0, total//cost1
    
        for i in range(max_val+1):
            remaining = total - cost1*i
            count += remaining//cost2 + 1

        return count

