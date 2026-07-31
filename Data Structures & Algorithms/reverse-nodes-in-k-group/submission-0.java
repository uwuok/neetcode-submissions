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
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null || k == 1) return head;
        ListNode dummy = new ListNode(0);
        dummy.next = head; 

        // 紀錄上一組的尾巴
        ListNode groupPrev = dummy;

        while (true) {
            // 先往後走 k steps 
            ListNode kth = getKth(groupPrev, k); 
            // if null, 表示剩餘不用翻轉
            if (kth == null) { break; }
            // 記錄下一組的開頭
            ListNode groupNext = kth.next; 
            ListNode curr = groupPrev.next;
            // 翻轉時把這組的尾巴連接到下一組的頭
            ListNode prev = groupNext;

            // reverse
            while (curr != groupNext) {
                ListNode next = curr.next; 
                curr.next = prev;
                prev = curr;
                curr = next; 
            }
            ListNode temp = groupPrev.next; 
            // reverse 後的第一個 element 連接到上一組的尾八
            groupPrev.next = kth; 
            // 移動到新尾八
            groupPrev = temp; 
        }
        return dummy.next; 
    }

    private ListNode getKth(ListNode cur, int k) {
        while (cur != null && k > 0) {
            cur = cur.next;
            --k;
        }
        return cur; 
    }
}
