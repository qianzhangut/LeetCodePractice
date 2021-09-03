class Solution:
    def secondHighest(self, s: str) -> int:
        l = []
        for i in s:
            if i.isdigit():
                l.append(i)

        res = sorted(list(set(l)))
        return res[-2] if len(res)>1 else -1
        
        
 
## two pointers
class Solution:
    def secondHighest(self, s: str) -> int:
        first = second = -1
        for c in s:
            if c.isdigit():
                d = int(c)
                if d > first:
                    first, second = d, first
                elif first > d > second:
                    second = d
        return second