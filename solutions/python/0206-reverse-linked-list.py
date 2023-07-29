class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        while head: 
            next_node = head.next 
            head.next = prev 
            prev = head 
            head = next_node 
        return prev 
