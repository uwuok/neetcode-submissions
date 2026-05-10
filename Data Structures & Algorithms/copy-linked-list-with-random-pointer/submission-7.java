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

        // copy 所有節點：<old_node, new_node>
        Node cur = head;
        while (cur != null) {
            nodeMap.put(cur, new Node(cur.val));
            cur = cur.next;
        }

        // 進行連接
        cur = head;
        while (cur != null) {
            Node copyNode = nodeMap.get(cur);  // deep copy
            copyNode.next = nodeMap.get(cur.next);
            copyNode.random = nodeMap.get(cur.random);
            cur = cur.next;
        }
        return nodeMap.get(head);
    }
}
