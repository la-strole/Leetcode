
 /* Definition for singly-linked list.*/
function ListNode(val) {
    this.val = val;
    this.next = null;
}
 
/**
 * @param {ListNode} node
 * @return {void} Do not return anything, modify node in-place instead.
 */
 var deleteNode = function(node) {
    
    let victim_node = node.next;

    node.val = victim_node.val;
    node.next = victim_node.next;

};