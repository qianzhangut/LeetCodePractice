class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        num = set("balloon")
        b = {'l': 2, 'o': 2, 'n': 1, 'b': 1, 'a': 1}
        d ={}
        for i in text:
            if i in num:
                d[i] = d.get(i, 0) + 1   
        res = []
        for key in d:
            res.append(d[key]/b[key])
            
        if len(res)<5:
            return 0
        elif len(set(res)) == 1:
            return int(res[0])
        else:
            return int(min(res))