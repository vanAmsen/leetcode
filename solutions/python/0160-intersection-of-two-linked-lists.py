# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB: 
            return None 

        # Step 1: Initialize two pointers 
        pA, pB = headA, headB 

        # Step 2: Determine the lengths of A and B 
        lenA, lenB = 0, 0 
        while pA: 
            lenA += 1 
            pA = pA.next 
        while pB: 
            lenB += 1 
            pB = pB.next 

        # Reset pointers to head 
        pA, pB = headA, headB 

        # Step 3: Adjust the starting position of the pointers 
        while lenA > lenB: 
            pA = pA.next 
            lenA -= 1 
        while lenB > lenA: 
            pB = pB.next 
            lenB -= 1 

        # Step 4: Move both pointers until they meet 
        while pA != pB: 
            pA = pA.next 
            pB = pB.next 

        # Return either one of the pointers 
        return pA 
                                                                                                                                                                                                                                                                                                                         
