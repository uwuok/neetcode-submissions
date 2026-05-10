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
        Map<Node, Node> nodeMap = new HashMap<>();
        Node cur = head;
        while (cur != null) {
            nodeMap.put(cur, new Node(cur.val)); // deep copy 
            cur = cur.next; 
        }

        cur = head; 
        while (cur != null) {
            Node copyNode = nodeMap.get(cur);
            copyNode.next = nodeMap.get(cur.next);
            copyNode.random = nodeMap.get(cur.random);
            cur = cur.next;
        }

        return nodeMap.get(head);
    }
}
