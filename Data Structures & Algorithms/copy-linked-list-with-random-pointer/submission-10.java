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
        // interwave
        // A -> A' -> B -> B' ...
        Node cur = head;
        while (cur != null) {
            Node clone = new Node(cur.val);
            clone.next = cur.next;
            cur.next = clone;
            cur = clone.next; // 走到下一個原節點
        }

        // 處理複製節點的 random pointer
        cur = head;
        while (cur != null) {
            // clone 的 random 指向 原本 random 的下一個 (也就是 clone 的 random)
            // 白話文：我分身的 random，要指向我本尊 random 目標的分身。
            if (cur.random != null) { cur.next.random = cur.random.next; }
            cur = cur.next.next; // 跳過 clone，走到下一個原節點
        }
        
        // 將交織的串列拆分成 原始串列 和 複製串列
        cur = head; 
        Node pseudoHead = new Node(0); // dummy node 方便操作新串列
        Node cloneCur = pseudoHead;

        while (cur != null) {
            cloneCur.next = cur.next; // 把分身接過來
            cloneCur = cloneCur.next; // 分身指標往前

            cur.next = cur.next.next; // 原本的串列恢復
            cur = cur.next;           // 遠本的指標往前
        }

        return pseudoHead.next; 
    }
}
