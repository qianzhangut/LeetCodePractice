class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans = 0
        n = len(words)
        for i in range(n):
            for j in range(i+1, n):
                if words[i]==words[j][::-1]:
                    ans += 1
        return ans