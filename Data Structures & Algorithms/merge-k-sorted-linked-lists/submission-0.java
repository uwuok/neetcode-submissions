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
        // edge case: if lists is empty, return null
        if (lists == null || lists.length == 0) {
            return null;
        }
        
        return mergeSort(lists, 0, lists.length - 1);
    }

    // divide
    public ListNode mergeSort(ListNode[] lists, int left, int right) {
        // base case: if left and right encounter, means only one list left.
        if (left == right) {
            return lists[left]; 
        }

        // find the middle of the lists
        int mid = left + (right - left) / 2; 

        // deal with left side using recursive.
        ListNode l1 = mergeSort(lists, left, mid);
        // deal with right side using recursive.
        ListNode l2 = mergeSort(lists, mid + 1, right);

        // 將處理好的 list 進行 merge
        return mergeTwoLists(l1, l2);
    }
    

    // conquer
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;

        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                cur.next = l1;
                l1 = l1.next;
            } else {
                cur.next = l2;
                l2 = l2.next;
            }
            cur = cur.next; 
        }
        cur.next = (l1 != null) ? l1 : l2;

        return dummy.next; 
    }
}
