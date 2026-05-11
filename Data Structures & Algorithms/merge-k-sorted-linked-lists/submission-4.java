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
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) { return null; }

        return mergeSort(lists, 0, lists.length - 1); 
    }

    public ListNode mergeSort(ListNode[] lists, int left, int right) {
        if (left == right) { return lists[left]; }

        int mid = left + (right - left) / 2;

        ListNode l1 = mergeSort(lists, left, mid);
        ListNode l2 = mergeSort(lists, mid + 1, right);

        return mergeTwoList(l1, l2);
    }

    // conquer 
    public ListNode mergeTwoList(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;

        // 將 list 中當前較小元素優先插入到新 list 中
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                cur.next = l1;
                l1 = l1.next;
                // cur = cur.next;
            } else {
                cur.next = l2;
                l2 = l2.next;
                // cur = cur.next; 
            }
            cur = cur.next; 
        }
        // 處理剩餘的 list
        cur.next = (l1 != null) ? l1 : l2;
        return dummy.next; 
    }
}
