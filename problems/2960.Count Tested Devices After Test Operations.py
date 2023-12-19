class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans = 0
        for i in batteryPercentages:
            ans += i>ans
        return ans
