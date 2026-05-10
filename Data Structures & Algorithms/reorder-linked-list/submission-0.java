/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public void reorderList(ListNode head) {
       
        ListNode slow = head;
        ListNode fast = head;
        // find mid
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode curr = slow;
        // reverse
        ListNode prev = null ;
        while (curr != null) {
            ListNode nxTemp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nxTemp;
        }
        // merge the two halves 
        ListNode first = head;
        ListNode second = prev;
        while (second.next != null) {
            ListNode tmp1 = first.next;
            ListNode tmp2 = second.next;
            first.next = second;
            second.next = tmp1;

            first = tmp1;
            second = tmp2; 
        }
    }
}
