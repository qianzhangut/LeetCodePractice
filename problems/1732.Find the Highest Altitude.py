class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans, alt = 0, 0
        
        for i in gain:
            alt += i
            if alt>ans:
                ans = alt
        return ans