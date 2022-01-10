/*
 * Definition for singly-linked list.
 */
class ListNode {
     int val;
     ListNode next;
     ListNode(int x) {
         val = x;
         next = null;
     }
}

public class Solution {
    public boolean hasCycle(ListNode head) {
        


        if (head == null || head.next == null || head.next.next == null){
            return false;
        }

        ListNode fast_ptr = head.next.next;
        ListNode slow_ptr = head.next;
       
        while (fast_ptr != slow_ptr){

            if (fast_ptr == null || fast_ptr.next == null){
                return false;
            }

            fast_ptr = fast_ptr.next.next;
            slow_ptr = slow_ptr.next;    

        }
        return true;
    }
}   