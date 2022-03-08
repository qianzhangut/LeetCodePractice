class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:

        n = [0]*1001
        for i in range(len(nums)-1):
            if nums[i]==key:
                n[nums[i+1]]+=1
        return n.index(max(n))