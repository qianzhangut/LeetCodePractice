class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        seen = set()
        for i, p in enumerate(password):
            if i>0 and p == password[i-1]:
                return False
            if p.isupper():
                seen.add('u')
            elif p.islower():
                seen.add('l')
            elif p.isdigit():
                seen.add('d')
            else:
                seen.add('s')


        return len(password)>7 and len(seen) == 4