class RedBlackTree<K extends Comparable<K>, V>{

    class RBNode{
        private K key;
        private V value;
        private boolean isBlack;

        private RBNode left = NIL;
        private  RBNode right = NIL;

        public RBNode(K key, V value) {
            this.key = key;
            this.value = value;
            this.isBlack = false;
        }

        public K getKey() {
            return key;
        }

        public V getValue() {
            return value;
        }

        public boolean isBlack() {
            return isBlack;
        }

        public void setKey(K key) {
            this.key = key;
        }

        public void setValue(V value) {
            this.value = value;
        }

        public void setIsBlack(boolean isBlack) {
            this.isBlack = isBlack;
        }

        public RBNode getLeft() {
            return left;
        }

        public void setLeft(RBNode left) {
            this.left = left;
        }

        public RBNode getRight() {
            return right;
        }

        public void setRight(RBNode right) {
            this.right = right;
        }
    }
    private final RBNode NIL = new RBNode(null, null);

    private RBNode root;
    public RedBlackTree() {
        this.root = NIL;
    }

    private RBNode find_node(K key) throws InvalidKeyException {
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
        throw new InvalidKeyException();

    }

    public V retrieve(K key) throws InvalidKeyException {
        var node = find_node(key);
        return node.getValue();

    }

    public void set(K key, V newValue) throws InvalidKeyException {
        var node = find_node(key);
        node.setValue(newValue);
    }

    public void insert(K key, V value) throws InvalidKeyException {
        var node = new RBNode(key,value);
        if (this.root == NIL){
            this.root = node;
        }
        else{
            var current = this.root;
            RBNode parent = null;
            while(current != NIL){
                if(current.getKey().equals(key)){
                    throw new InvalidKeyException();
                }
                var comp = current.getKey().compareTo(key);
                parent = current;
                if(comp < 0){

                }
            }
        }
    }
}