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

        // divide: 以兩兩一組的方式進行合併
        int amount = lists.length;  // 總共需要合併的數量
        int interval = 1;           // 兩兩合併時的間隔

        // 當間隔小於總數時，持續進行兩兩合併
        while (interval < amount) {
            // 注意，這裡並沒有更新 interval 的值
            for (int i = 0; i < amount - interval; i += interval * 2) {
                lists[i] = mergeTwoList(lists[i], lists[i + interval]);
            }
            // 間隔翻倍 (1 -> 2 -> 4 -> 8)
            interval *= 2; 
        }
        return lists[0];
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
                cur = cur.next;
            } else {
                cur.next = l2;
                l2 = l2.next;
                cur = cur.next; 
            }
        }
        // 處理剩餘的 list
        cur.next = (l1 != null) ? l1 : l2;
        return dummy.next; 
    }
}
