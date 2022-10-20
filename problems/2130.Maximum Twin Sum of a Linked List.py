# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = []
        while head:
            n.append(head.val)
            head = head.next
        s = 0
        for x, y in enumerate(n):
            s = max(s, y+n[len(n)-x -1])
            
        return ss
        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverseList(node): # reverse the linked list starting from node and return the reversed list 
            prev = None
            while node:
                temp = node.next 
                node.next = prev
                prev = node
                node = temp
            return prev
            
        ans = 0
        slow, fast = head, head
        while fast and fast.next: 
            fast = fast.next.next
            slow = slow.next
        # now slow pointer points to the start node of the right half of the linked list
        
        slow = reverseList(slow)
        while slow:
            ans = max(ans, slow.val + head.val)
            slow = slow.next
            head = head.next
        
        return ans