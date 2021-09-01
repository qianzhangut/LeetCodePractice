class Solution:
    def secondHighest(self, s: str) -> int:
        l = []
        for i in s:
            if i.isdigit():
                l.append(i)

        res = sorted(list(set(l)))
        return res[-2] if len(res)>1 else -1