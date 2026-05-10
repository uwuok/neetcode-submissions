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
        // build a interwave list
        // A -> A' -> B -> B'
        Node cur = head;
        while (cur != null) {
            Node clone = new Node(cur.val);
            clone.next = cur.next;
            cur.next = clone;
            cur = clone.next; // 跳過 clone node
        }

        // 處理 random
        cur = head;
        while (cur != null) {
            if (cur.random != null) { 
                // clone node 的 random = cur random 的 clone node
                cur.next.random = cur.random.next;
            }
            cur = cur.next.next;
        }

        // split ori list and clone list
        Node dummy = new Node(-1);
        cur = head;
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
