class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        a1, cnt  = 1, 0 
        for i in s:
            cnt += widths[ord(i)-97]
            if cnt > 100:
                cnt = widths[ord(i)-97]
                a1 += 1
            
        return [a1, cnt]
            