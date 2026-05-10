class LRUCache {

    private int capacity;
    private Deque<Integer> deque;
    private HashMap<Integer, Integer> table;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        deque = new LinkedList<Integer>();
        table = new HashMap<Integer, Integer>(capacity);
    }
    
    public int get(int key) {
        if (table.containsKey(key)) {
            deque.remove(key);
            deque.addLast(key);
            return table.get(key);
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if (table.containsKey(key)) {
            // table[key] = value;
            table.replace(key, value);
            deque.remove(key);
            deque.addLast(key);
        } else {
            if (table.size() < capacity) {
                table.put(key, value);
            } else {
                table.remove(deque.getFirst());
                deque.removeFirst();
                table.put(key, value);
            }
            deque.addLast(key);
        }
    }
}
