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
        // l1 = [9], l2 = [9]
        // output = 9 + 9 = 18 
        // reverse store: [8, 1]
        ListNode cur1 = l1;
        ListNode cur2 = l2;
        ListNode dummy = new ListNode(-1);
        ListNode dcur = dummy;
        // int sz = 0;
        int carry = 0;
        while (cur1 != null || cur2 != null) {
            int sum = carry;

            if (cur1 != null) {
                sum += cur1.val;
                cur1 = cur1.next;
            }

            if (cur2 != null) {
                sum += cur2.val;
                cur2 = cur2.next;
            }

            dcur.next = new ListNode(sum % 10);
            carry = sum / 10;
            dcur = dcur.next;
        }

        
        if (carry != 0) {
            dcur.next = new ListNode(carry);
        }

        return dummy.next;
    }
}
