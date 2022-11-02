class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[1]]
        for i in range(1, rowIndex+1):
            temp1 = ans[-1] + [0]
            temp2 = [0] + ans[-1]
            ans.append([temp1[j]+ temp2[j] for j in range(len(temp1))])
            
        return ans[-1]