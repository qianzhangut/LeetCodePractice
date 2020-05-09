# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        cur = head
        while cur.next and cur:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head