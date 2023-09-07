class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0, head)
        prev = dummy
        
        for _ in range(left - 1):
            prev = prev.next
        
        current = prev.next
        
        for _ in range(right - left):
            next_node = current.next
            current.next, next_node.next, prev.next = next_node.next, prev.next, next_node

        return dummy.next
