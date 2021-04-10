class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for str in zip(*strs):
            if any(str[i]>str[i+1] for i in range(len(str)-1)):
                ans += 1
                
        return ans