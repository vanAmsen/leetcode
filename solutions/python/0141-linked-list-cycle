# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_pointer = head 
        fast_pointer = head 
        while fast_pointer and fast_pointer.next: 
            slow_pointer = slow_pointer.next 
            fast_pointer = fast_pointer.next.next 
            if slow_pointer == fast_pointer: 
                return True 
        return False 
                                                                                            
