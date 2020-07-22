class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [ 'a', 'e', 'i', 'o', 'u']
        indices, chars = [], []
        for i in range(len(s)):
            chars.append(s[i])
            if s[i].lower() in vowels:
                indices.append(i)

        left, right = 0, len(indices)-1
        while left < right:
            p, q = indices[left], indices[right]
            chars[p], chars[q] = chars[q], chars[p]
            left += 1
            right -= 1

        return ''.join(chars)