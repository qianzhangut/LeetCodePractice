# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

       if not l1:
        return l2
       if not l2:
        return l1
    
       if l1.val+l2.val<10:
        l3=ListNode(l1.val+l2.val)
        l3.next=self.addTwoNumbers(l1.next,l2.next)
       elif l1.val+l2.val>=10:
        l3 = ListNode(l1.val + l2.val - 10)
        carry=ListNode(1)
      
        l3.next=self.addTwoNumbers(l1.next,self.addTwoNumbers(l2.next, carry))
       return l3
        
            
                
        