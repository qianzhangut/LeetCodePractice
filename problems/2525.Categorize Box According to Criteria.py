class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        idx = int(length >= 10000 or width >= 10000 or height >= 10000 or 
        length * width * height >= 10**9) + 2*(mass >= 100)
        
        return ("Neither", "Bulky", "Heavy", "Both")[idx]