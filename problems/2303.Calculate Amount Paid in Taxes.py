class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        prev, tax = 0, 0
        
        for i, j in brackets:
            i = min(i, income)
            tax += (i-prev)*j/100
            prev = i
        return tax
                