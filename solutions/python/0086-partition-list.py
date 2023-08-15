class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before, after = ListNode(0), ListNode(0) 
        before_curr, after_curr = before, after 

        while head: 
            if head.val < x: 
                before_curr.next, before_curr = head, head 
            else: 
                after_curr.next, after_curr = head, head 
            head = head.next 

        after_curr.next = None 
        before_curr.next = after.next 

        return before.next 
