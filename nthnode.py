class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start=ListNode(0)
        start.next=head
        slow=start
        fast=start
        for i in range(n):
            fast=fast.next
        while(fast.next != None):
            fast=fast.next
            slow=slow.next
            
        slow.next=slow.next.next
        return start.next
        
        
