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
        ListNode fast = head;
        ListNode slow = head;
        // find the mid of node
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        // reverse the split or right
        ListNode curr = slow; 
        ListNode prev = null;
        while (curr != null) {
            ListNode nxtemp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nxtemp;
        }
        // merge two halves
        ListNode left = head;
        ListNode right = prev; // or slow?
        while (right.next != null)  {
            ListNode tmp1 = left.next;
            ListNode tmp2 = right.next;
            // tmp1.next = tmp2;
            // tmp2.next = tmp1;
            left.next = right;
            right.next = tmp1;

            left = tmp1;
            right = tmp2; 
        }
    }
}
