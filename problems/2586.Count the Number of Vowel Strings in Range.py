class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vow = set(['a', 'e', 'i', 'o', 'u'])
        ans = 0
        for i in words[left:right+1]:
            if (i[0] in vow) and (i[-1] in vow):

                ans += 1

        return ans
        
        
##
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = set('aeiou')
        
        return sum({w[0],w[-1]}.issubset(vowels) for w in words[left:right+1])