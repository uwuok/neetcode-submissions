class Node {
    int key;
    int value;
    Node prev;
    Node next; 

    public Node(int key, int value) {
        this.key = key;
        this.value = value; 
    }
}

class LRUCache {
    
    private Map<Integer, Node> cache;
    private int capacity;
    private Node left;
    private Node right; 

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>(); 
        this.left = new Node(0, 0);
        this.right = new Node(0, 0);
        this.left.next = this.right;
        this.right.prev = this.left; 
    }

    public void remove(Node node) {
        Node prev = node.prev;
        Node next = node.next;
        prev.next = next;
        next.prev = prev;
    }

    public void insert(Node node) {
        Node prev = this.right.prev; 
        prev.next = node;
        node.prev = prev; 
        node.next = this.right;
        this.right.prev = node; // why don't we use "prev = node;" ? 
    }

    public int get(int key) {
        if (cache.containsKey(key)) {
            Node node = cache.get(key);
            remove(node);
            insert(node);
            return node.value; 
        }
        return -1; 
    }
    
    public void put(int key, int value) {
        // update, but we need to let the newlest key put at the begining.
        if (cache.containsKey(key)) {
            // use remove to avoid the approch capacity limit. 
            remove(cache.get(key));
        }
        Node newNode = new Node(key, value);
        cache.put(key, newNode);
        insert(newNode);

        if (cache.size() > this.capacity) {
            Node lru = this.left.next; // what is "this" element? is it always the element at the least of cache?
            remove(lru); // could we just use "remove(newNode.prev)" ?
            cache.remove(lru.key);
        }
    }
}
