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
        
## o(1) space solution

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i, j = 0, 1
        n = len(nums)
        
        while i<n and j <n:
            if nums[i]%2 == 0:
                i += 2
            elif nums[j]%2 == 1:
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
        return nums