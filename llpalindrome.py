class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        prv=None
        while slow:
            temp=slow.next
            slow.next=prv
            prv=slow
            slow=temp
        l,r=head,prv
        while r:
            if l.val!=r.val:
                return False
            l=l.next
            r=r.next
        return True
        
