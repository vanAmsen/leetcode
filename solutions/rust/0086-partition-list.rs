impl Solution {
    pub fn partition(mut head: Option<Box<ListNode>>, x: i32) -> Option<Box<ListNode>> {
        let mut before = ListNode::new(0); 
        let mut after = ListNode::new(0); 
        let mut before_tail = &mut before; 
        let mut after_tail = &mut after; 

        while let Some(mut node) = head { 
            head = node.next.take(); 
            if node.val < x { 
                before_tail.next = Some(node); 
                before_tail = before_tail.next.as_mut().unwrap(); 
            } else { 
                after_tail.next = Some(node); 
                after_tail = after_tail.next.as_mut().unwrap(); 
            } 
        } 

        before_tail.next = after.next.take(); 

        before.next 
                                                                                                                                                              
    }
}
