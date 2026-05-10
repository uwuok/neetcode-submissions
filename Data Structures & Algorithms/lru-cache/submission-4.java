class LRUCache {

    Map<Integer, Node> cache;
    int capacity;
    Node left;
    Node right;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>();
        this.left = new Node(0, 0);
        this.right = new Node(0, 0);
        this.left.next = this.right; // the oldest element
        this.right.prev = this.left; // the newest element
    }

    public void remove(Node node) {
        Node prev = node.prev;
        Node next = node.next;
        prev.next = next;
        next.prev = prev; 

        // Node prev = node.prev;
        // prev.next = node.next;
        // prev.next.prev = prev; 
    }

    public void insert(Node node) {
        Node prev = this.right.prev; // get the newest element in the cache(this.right.prev)
        prev.next = node;            // add the new element to the cahce be
        node.prev = prev;
        node.next = this.right;
        this.right.prev = node;
    }
    
    public int get(int key) {
        if (cache.containsKey(key)) {
            Node node = cache.get(key);
            remove(node);
            insert(node);
            return node.val;
        }
        return -1; 
    }
    
    public void put(int key, int value) {
        Node newNode = new Node(key, value);
        cache.put(key, newNode);
        insert(newNode);

        if (cache.size() > capacity) {
            Node lru = this.left.next;
            remove(lru); // remove the oldest element
            cache.remove(lru.key); 
        }
    }
}

class Node {
    int key;
    int val;
    Node next;
    Node prev;

    public Node(int key, int val) {
        this.key = key;
        this.val = val;
        this.next = null;
        this.prev = null;
    }
}