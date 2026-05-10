/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        // interwave node
        // A -> A' -> B -> B' ...
        Node cur = head;
        while (cur != null) {
            Node clone = new Node(cur.val);
            clone.next = cur.next;
            cur.next = clone;
            cur = clone.next; 
        }

        // 處理 random (interwave 後沒有改變原本節點對於 random 的連接)
        cur = head; 
        while (cur != null) {
            if (cur.random != null) {
                // 複製品的 random = 當前 random 目標的複製品
                cur.next.random = cur.random.next; 
            }
            cur = cur.next.next; // 跳過 clone node
        }

        // 拆分原節點和 clone 節點
        cur = head;
        Node dummy = new Node(-1);
        Node cloneCur = dummy;
        while (cur != null) {
            cloneCur.next = cur.next;
            cloneCur = cloneCur.next;
            cur.next = cur.next.next;
            cur = cur.next; 
        }
        return dummy.next;
    }
}
