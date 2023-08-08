# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Helper function to compute GCD using Euclidean algorithm 
        def gcd(a, b): 
            while b: 
                a, b = b, a % b 
            return a 
        # Base case: if head is None or there's only one node 
        if not head or not head.next: 
            return head 
        # Initialize the current pointer 
        current = head 
        # Traverse the linked list 
        while current and current.next: 
            # Compute the GCD of current and current's next values 
            gcd_val = gcd(current.val, current.next.val) 
            # Create a new node with the computed GCD value 
            new_node = ListNode(gcd_val) 
            # Insert the new node between current and current.next nodes 
            new_node.next = current.next 
            current.next = new_node 
            # Move to the next node (skip the inserted node) 
            current = new_node.next 
        return head       
                                                                                                                                                                                                                                          
