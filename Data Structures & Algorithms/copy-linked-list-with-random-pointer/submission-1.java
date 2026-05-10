class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) { return null; }

        List<Node> oldList = new ArrayList<>();
        List<Node> newList = new ArrayList<>();

        // 第一階段：把舊節點依序存入 oldList，同時創造新節點存入 newList
        Node cur = head;
        while (cur != null) {
            oldList.add(cur);
            newList.add(new Node(cur.val));
            cur = cur.next;
        }

        // 第二階段：把 newList 裡的新節點的 next 全部串接起來
        for (int i = 0; i < newList.size() - 1; i++) {
            newList.get(i).next = newList.get(i + 1);
        }

        // 第三階段：處理 random 指標 (你的卡關點)
        for (int i = 0; i < oldList.size(); i++) {
            Node oldNode = oldList.get(i);
            
            if (oldNode.random != null) {
                // 關鍵：找出舊的 random 節點，在舊 List 中是「第幾個索引 (Index)」
                int randomIndex = oldList.indexOf(oldNode.random);
                
                // 讓新節點的 random，指向新 List 中相同索引位置的節點
                newList.get(i).random = newList.get(randomIndex);
            }
        }

        // 回傳新 List 的第一個節點 (head)
        return newList.get(0);
    }
}