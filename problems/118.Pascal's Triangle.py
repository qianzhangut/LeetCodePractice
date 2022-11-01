class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1,numRows):
            temp1 = ans[-1] + [0]
            temp2 = [0] + ans[-1]
            ans.append([temp1[i]+temp2[i] for i in range(len(temp1))])
            
        return ans