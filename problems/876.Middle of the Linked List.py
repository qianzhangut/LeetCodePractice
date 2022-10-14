# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = head, head
        
        while cur and cur.next:
            cur = cur.next.next
            pre = pre.next
            
        return pre