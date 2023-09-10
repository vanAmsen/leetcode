func reverseList(head *ListNode) *ListNode {  
    var prev *ListNode 
    curr := head 
    for curr != nil { 
            nextTemp := curr.Next 
        curr.Next = prev 
        prev = curr 
        curr = nextTemp 
    } 
    return prev 
} 
                                     
func pairSum(head *ListNode) int {
        // Find the middle node 
    slow, fast := head, head 
    for fast != nil && fast.Next != nil { 
        slow = slow.Next 
        fast = fast.Next.Next 
    } 

    // Reverse the second half of the linked list 
    slow = reverseList(slow) 

    // Calculate the maximum twin sum 
    maxSum := 0 
    first, second := head, slow 
    for second != nil { 
        sum := first.Val + second.Val 
        if sum > maxSum { 
            maxSum = sum 
        } 
        first = first.Next 
        second = second.Next 
    } 

    return maxSum 
                                                                                                                            
}
