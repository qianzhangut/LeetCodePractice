class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a_real = int(a[:-1].split("+")[0])
        a_img = int(a[:-1].split("+")[1])
        b_real = int(b[:-1].split("+")[0])
        b_img = int(b[:-1].split("+")[1])
        
        return str(a_real*b_real-a_img*b_img) + "+" + str(a_img*b_real+a_real*b_img) + "i"