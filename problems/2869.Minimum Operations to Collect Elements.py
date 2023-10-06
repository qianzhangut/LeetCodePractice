class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        for i in range(len(nums)-1, -1, -1):
            if set(range(1,k+1)).issubset(set(nums[i:])):
                return len(nums)-i
                
#set             
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        st  = set()
        for i in range(len(nums)-1, -1, -1):
            if nums[i] <= k:
                st.add(nums[i])
            if len(st) == k:
                return len(nums)-i
