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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int reminder = 0;
        ListNode head = new ListNode(); 
        ListNode cur = head;
        while (l1 != null || l2 != null || reminder != 0) {
            int v1 = (l1 != null ? l1.val : 0);
            int v2 = (l2 != null ? l2.val : 0);
            int sum = v1 + v2 + reminder;  
            reminder = sum / 10;
            cur.next = new ListNode(sum % 10);
            cur = cur.next;
            if (l1 != null)
                l1 = l1.next;
            if (l2 != null)
                l2 = l2.next;
            
        }
        return head.next;
    }
}
