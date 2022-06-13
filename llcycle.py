class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head==None or head.next==None:
            return False
        slow=ListNode()
        fast=ListNode()
        slow=head
        fast=head
        
        while fast.next != None and fast.next.next!=None:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                return True
       
        return False
        
