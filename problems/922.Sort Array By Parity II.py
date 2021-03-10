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