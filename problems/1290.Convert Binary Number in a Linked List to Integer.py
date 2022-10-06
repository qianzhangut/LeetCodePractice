# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        p, res = 0, []
        while head:
            p += 1
            res.append(head.val)
            head = head.next

        
        return sum([res[i]*2**(p-i-1) for  i in range(p)])