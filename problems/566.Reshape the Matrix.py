
### flat the list

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums)*len(nums[0]) != r*c:
            return nums
        new = [j for i in nums for j in i]
        
        res = []
        for i in range(0, len(new), c):
            res.append(new[i:i+c]) 
        return res

### brutal force


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        
        rows = len(nums)
        cols = len(nums[0])
        
        
        if r*c == rows*cols: #pass only the dimensions match
            d = [[0]*c for i in range(r)]
        
            row_nums = 0
            col_nums = 0
            #simply Traverse through the nums array
            
			for i in range(0,rows):
                for j in range(0,cols):
                    d[row_nums][col_nums] = nums[i][j]
                    col_nums +=1
                    if col_nums == c: #traverse until a column is complete in a row
                        row_nums +=1 
                        col_nums = 0 #restart the column for new row
                        
            return d
 
        else:
            return nums