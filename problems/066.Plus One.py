class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ''.join(str(i) for i in digits)
        number = int(number)+1
        return list(str(number))