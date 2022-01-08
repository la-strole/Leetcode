/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
 var isPalindrome = function(head) {
    // Border cases
    if (! head.next || ! head){
        return true;
    }

    

    // Find the middle slow_ptr - head
    let slow_ptr = head;
    let fast_ptr = head;
    while (fast_ptr && fast_ptr.next){
        fast_ptr = fast_ptr.next.next;
        slow_ptr = slow_ptr.next;
    }

    // Reverse second part ptr0 - head
    let ptr0 = null;
    let ptr1 = slow_ptr;

    while(ptr1){
        let ptr2 = ptr1.next;
        ptr1.next = ptr0;
        ptr0 = ptr1;
        ptr1 = ptr2;
    }

    // Find if it is palindrome
    while (head && ptr0){
        if (head.val != ptr0.val){
            return false;
        }
        head = head.next;
        ptr0 = ptr0.next;
    }
    return true;


};