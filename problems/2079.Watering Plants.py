class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans, cc = 0, capacity
        for i in range(len(plants)):
            if cc < plants[i]:
                ans += 2*i
                cc = capacity
            ans += 1
            cc -= plants[i]
        return ans