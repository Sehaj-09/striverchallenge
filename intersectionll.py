class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA ==None or headB== None:
            return None
        d1=ListNode()
        d1=headA
        d2=ListNode()
        d2=headB
        
        while d1!= d2:
            d1 = headB if d1 is None else d1.next
            d2 = headA if d2 is None else d2.next
        return d1
