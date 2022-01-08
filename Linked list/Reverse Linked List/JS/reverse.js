/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
 var reverseList = function(head) {
    ptr0 = null;
    ptr1 = head
    
    while (ptr1){
        ptr2 = ptr1.next;
        ptr1.next = ptr0;
        ptr0 = ptr1;
        ptr1 = ptr2;
    }

    return ptr0;

};