class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        num1, num2 = [], []
        
        for i in nums:
            if i%2==1:
                num1.append(i)
            else:
                num2.append(i)
        
        ans = [0]*len(nums)
        
        ans[::2] = num2
        ans[1::2] = num1           
        
        return ans
        
        
##simplified version
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        ans[::2] = [i for i in nums if i%2==0]
        ans[1::2] = [j for j in nums if j%2==1]      
        
        return ans
        
