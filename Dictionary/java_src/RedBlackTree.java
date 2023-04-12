class RedBlackTree<K extends Comparable<K>, V>{
    static final RBNode NIL = new RBNode(null, null);

    private RBNode<K,V> root;
    public RedBlackTree() {
        this.root = NIL;
    }

    private RBNode<K, V> find_node(K key) throws KeyErrorException{
        var current = this.root;
        while (current != NIL){
            var comp = key.compareTo(current.getKey());
            if (comp == 0){
                return current;
            }
            else if (comp < 0) {
                current = current.getLeft();
            }
            else{
                current = current.getRight();
            }
        }
        throw new KeyErrorException();

    }

    public V retrieve(K key) throws KeyErrorException{
        var node = find_node(key);
        return node.getValue();

    }

    public void set(K key, V newValue) throws KeyErrorException {
        var node = find_node(key);
        node.setValue(newValue);
    }
}