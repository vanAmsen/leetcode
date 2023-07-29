/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    let prev = null;
    while (head) {
        let next_node = head.next;
        head.next = prev;
        prev = head;
        head = next_node;
    }
    return prev;    
};
