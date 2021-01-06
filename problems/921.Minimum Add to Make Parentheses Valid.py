class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        left, right = 0, 0
        for i in S:
            if i == "(":
                right += 1
            elif i == ")" and right > 0 :
                right -=1
            elif i == ")" and right == 0:
                left += 1
        return left + right