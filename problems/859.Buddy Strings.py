class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        if len(a) != len(b): return False
        if a == b and len(set(a)) < len(a): return True
        dif = [(i,j) for i, j in zip(a,b) if i!=j]
        return len(dif) == 2 and dif[0] == dif[1][::-1]