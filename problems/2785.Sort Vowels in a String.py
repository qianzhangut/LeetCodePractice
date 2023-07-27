class Solution:
    def sortVowels(self, s: str) -> str:
        sl , v, pos, vs = list(s), [], [], set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        for x, y in enumerate(sl):
            if y in vs:
                v.append(y)
                pos.append(x)

        v.sort()
        for i, c in zip(pos, v):
            sl[i]=c
        return ''.join(sl)