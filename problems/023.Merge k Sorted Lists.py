# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        k=len(lists)
        if k==0:
            return None
        mergedList = lists[0]
        for i in range(1,k):
            mergedList =self.mergeTwoLists(mergedList, lists[i])
        return mergedList
        
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        dummy = ListNode(0)
        nextNode = dummy
        while l1 and l2:
            if l1.val > l2.val:
                nextNode.next = l2
                nextNode = nextNode.next
                l2 = l2.next
            else:
                nextNode.next = l1
                nextNode = nextNode.next
                l1 = l1.next
        
        if l1:
            nextNode.next = l1
            
        if l2:
            nextNode.next = l2
        
        return dummy.next
        