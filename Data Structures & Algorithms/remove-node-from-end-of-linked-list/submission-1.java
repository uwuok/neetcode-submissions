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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // 如果直接 reverse 最後 output 時，也需要 reverse 回來

        // 判斷有多少的 node
        ListNode curr = head;
        int sz = 1;
        while (curr.next != null) {
            curr = curr.next;
            sz++;
        }


        // remove the nth node
        // head = [1, 2, 3, 4, 5, 6], n = 2 
        // res = [1, 2, 3, 4, 6]
        int target = sz - n; // 0-base 
        if (target == 0) return head.next; 


        ListNode prev = head;
        for (int i = 0; i < target - 1; ++i) {
            prev = prev.next;
        }

        prev.next = prev.next.next;
        
        return head; 
    }
}
