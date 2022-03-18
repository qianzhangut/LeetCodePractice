class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ans = []
        left, right = 0, sum(nums)
        ans = [left+right]
        for i in range(len(nums)):
            if nums[i] == 0:
                left +=1
            else:
                right -=1
            ans.append(left+right)
        m = max(ans)          
        return [j for j in range(len(ans)) if ans[j]==m]