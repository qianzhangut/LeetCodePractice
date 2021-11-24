# brutal force

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = -1
        for i in range(len(colors)):
            for j in range(i, len(colors)):
                if colors[i] != colors[j]:
                    ans = max(ans, abs(i-j))
        return ans
        
        
# O(n)

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = -1
        for i in range(len(colors)):
                if colors[i] != colors[0]:
                    ans = max(ans, abs(i-0))

                if colors[i] !=colors[-1]:
                    ans = max(ans, abs(len(colors)-i-1))
        return ans