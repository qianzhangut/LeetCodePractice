class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans = 0
        for i in batteryPercentages:
            ans += i>ans
        return ans

#brutal force
class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans = 0
        n = len(batteryPercentages)
        for i in range(n):
            if batteryPercentages[i] >0:
                ans += 1
                for j in range(i+1, n):
                    batteryPercentages[j] = max(0, batteryPercentages[j] - 1)
            

        return ans
