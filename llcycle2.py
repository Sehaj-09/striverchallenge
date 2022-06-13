class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return None 
        slow=ListNode()
        fast=ListNode()
        entry=ListNode
        slow=head
        fast=head
        entry=head
        
        while fast.next != None and fast.next.next!=None:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                while slow!=entry:
                    slow=slow.next
                    entry=entry.next
                return entry
        return None
