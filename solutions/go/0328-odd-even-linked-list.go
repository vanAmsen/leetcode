func oddEvenList(head *ListNode) *ListNode {
    if head == nil || head.Next == nil { 
        return head 
    } 

    odd := head 
    even := head.Next 
    evenHead := even 

    for even != nil && even.Next != nil { 
        // Move odd node 
        odd.Next = even.Next 
        odd = odd.Next 

        // Move even node 
        even.Next = odd.Next 
        even = even.Next 
    } 

    // Link last odd node to the head of even list 
    odd.Next = evenHead 

    return head 
                                                                                                                   
}
