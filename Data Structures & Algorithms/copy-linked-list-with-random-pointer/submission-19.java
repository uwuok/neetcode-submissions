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
        // interwave the list
        // A -> A' -> B -> B' ...
        Node cur = head;
        while (cur != null) {
            Node copy = new Node(cur.val);
            copy.next = cur.next;
            cur.next = copy;
            cur = copy.next; 
        }

        // deal with random
        cur = head;
        while (cur != null) {
            if (cur.random != null) {
                // 當前節點的複製品的 random = 當前節點的 random 的複製品
                // 假設 cur 是原節點 A
                // cur.next 指向 A'
                // cur.random 指向 C
                // cur.random.next 就指向 C' 
                // A' 的 random 指向 C' 
                cur.next.random = cur.random.next; 
            }
            cur = cur.next.next; // jumps to clone node
        }

        // split clone list and ori list
        cur = head;
        Node dummy = new Node(-1);
        Node cloneCur = dummy; 
        // A -> A' -> B -> B' ...
        // A -> B ...
        // d -> A' -> B' ...
        while (cur != null) {
            cloneCur.next = cur.next;
            cloneCur = cloneCur.next;
            cur.next = cloneCur.next;
            cur = cur.next;
        }
        return dummy.next;
    }
}
