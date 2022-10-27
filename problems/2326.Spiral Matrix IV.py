# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1 for i in range(n)] for j in range(m)]
        
        dx,dy,x,y = 1,0,0,0
        
        while head:
            res[y][x] = head.val
            if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= m or res[y+dy][x+dx] != -1:
                dx, dy = -dy, dx
            x = x + dx
            y = y + dy
            head = head.next
        return res