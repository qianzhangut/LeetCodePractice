class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        test = ['0'*i + '1'*i for i in range(26)]

        for j in test[::-1]:
            if j in s:
                return len(j)

        return 0