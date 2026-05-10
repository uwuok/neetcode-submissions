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
        // A -> A' -> B -> B'
        Node cur = head;
        while (cur != null) {
            Node clone = new Node(cur.val);
            clone.next = cur.next;
            cur.next = clone;
            cur = clone.next;
        }

        // deal with random
        cur = head;
        while (cur != null) {
            if (cur.random != null) {
                // clone node's random = origin node random's clone 
                cur.next.random = cur.random.next;
            }
            cur = cur.next.next; // jumps over the clone node
        }

        // split origin and clone node
        // A -> A' -> B -> B'
        cur = head;
        Node dummy = new Node(-1);
        Node cloneCur = dummy;
        while (cur != null) {
            cloneCur.next = cur.next;
            cloneCur = cloneCur.next;
            cur.next = cloneCur.next;
            cur = cur.next;
        }
        return dummy.next; 
    }
}
