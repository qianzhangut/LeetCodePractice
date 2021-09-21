class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        cnt = 0
        for item in patterns:
            if item in word:
                cnt += 1
                
        return cnt