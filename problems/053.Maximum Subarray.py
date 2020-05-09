class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
 
        dp, m_sum = nums[0], nums[0]
        for i in range(1,n):
            dp = max(dp+nums[i], nums[i])
            m_sum = max(dp,m_sum)
        return m_sum