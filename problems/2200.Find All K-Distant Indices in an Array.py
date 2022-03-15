class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        kc = [i for i in range(len(nums)) if nums[i] == key]
        ans = []
        for j in kc:
            ans += list(range(max(j-k, 0), min(j+k+1, len(nums))))
                
        return list(set(ans))