class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d = {}
        for item in arr:
            if item not in d:
                d[item] = 1 
            else:
                d[item] += 1
            if d[item]/len(arr)>0.25:
                return item
                
                
# Binary search

def findIndexOfFirst(x):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return l

for q in range(1, 4):
    idx = int(q * len(arr) / 4)
    start = findIndexOfFirst(arr[idx])
    if arr[start] == arr[start + len(arr)//4]:  
        return arr[start]