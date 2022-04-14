class Solution:
    def largestInteger(self, num: int) -> int:
        n = len(str(num))
        arr = [int(i) for i in str(num)]
        odd, even = sorted([str(i) for i in arr if i%2!=0]), sorted([str(j) for j in arr if j%2==0])
        res = ''
        for i in range(n):
            if arr[i] % 2 == 0:
                res += even.pop()
            else:
                res += odd.pop()
        return res