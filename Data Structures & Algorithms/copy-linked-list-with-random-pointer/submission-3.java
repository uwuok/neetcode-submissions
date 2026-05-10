class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) { return null; }

        // 使用 HashMap 來保存對應關係：<舊節點, 新節點>
        Map<Node, Node> nodeMap = new HashMap<>();

        Node cur = head;
        
        // 第一階段：單純複製所有節點，並存入 Map 中 (deep copy)
        while (cur != null) {
            nodeMap.put(cur, new Node(cur.val));
            cur = cur.next; 
        }

        cur = head;
        // 第二階段：處理所有的 next 和 random 指標
        while (cur != null) {
            // 從 Map 中拿出目前節點的「複製品」
            Node copyNode = nodeMap.get(cur);
            
            // 將複製品的 next 指向：舊節點 next 的「複製品」
            copyNode.next = nodeMap.get(cur.next);
            
            // 將複製品的 random 指向：舊節點 random 的「複製品」
            copyNode.random = nodeMap.get(cur.random);
            
            cur = cur.next; 
        }

        // 回傳 head 對應的複製品，即為新 List 的起點
        return nodeMap.get(head); 
    }
}