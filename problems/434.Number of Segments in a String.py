## use strip and split

class Solution:
    def countSegments(self, s: str) -> int:
        res = [i.strip() for i in s.split(" ") if i.strip()]
        return len(res)