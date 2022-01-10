/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
 var hasCycle = function(head) {
    
    // If there is 0 or 1 node
    if (! head || ! head.next){
        return false;
    }

    let slow_ptr = head;
    let fast_ptr = head.next;

    while (slow_ptr != fast_ptr){
        if (! fast_ptr.next || ! fast_ptr.next.next){
            return false;
        }
        slow_ptr = slow_ptr.next;
        fast_ptr = fast_ptr.next.next;
    }
    return true;

};