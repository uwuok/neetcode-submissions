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
        ListNode dummy = new ListNode(-1, head);
        ListNode left = dummy;
        ListNode right = head;

        // 先移動 right，使其與 left 相差 n 個距離
        while (n > 0) {
            --n;
            right = right.next;
        }

        // 移動 right 直到 list 的結尾，此時 left 會位於刪除節點的前一個節點前
        while (right != null) {
            left = left.next;
            right = right.next;
        }
        
        left.next = left.next.next;
        return dummy.next;
    }
}
