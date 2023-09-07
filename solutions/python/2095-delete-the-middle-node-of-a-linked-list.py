class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # First pass: Find the length of the linked list 
        length = 0 
        curr = head 
        while curr: 
            length += 1 
            curr = curr.next 

        # Special case: if the list has only one node, return None 
        if length == 1: 
            return None 

        # Initialize pointers for the second pass 
        curr = head 
        prev = None 

        # Second pass: Find and delete the middle node 
        for i in range(length // 2): 
            prev = curr 
            curr = curr.next 

        # Delete the middle node 
        if prev: 
            prev.next = curr.next 
        else: 
            head = curr.next  # Update head if the list had only two nodes 

        return head 
                                                                                                                                                                                                                                                          
