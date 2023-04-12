class RedBlackTree<K extends Comparable<K>, V>{

    private class RBNode{
        private K key;
        private V value;
        private boolean isBlack;

        private RBNode parent = null;

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

        public RBNode getLeftChild() {
            return left;
        }

        public void setLeftChild(RBNode left) {
            this.left = left;
            if(left != NIL){
                left.parent = this;
            }

        }

        public RBNode getRightChild() {
            return right;
        }

        public void setRightChild(RBNode right) {
            this.right = right;
            if(right != NIL){
                right.parent = this;
            }
        }

        public RBNode getParent() {
            return parent;
        }

        public void setParent(RBNode parent) {
            if(this != NIL){  // NIL has no parent
                this.parent = parent;
            }
        }

        public boolean isLeftChild(){
            if (this.parent == NIL){
                return false;
            }
            var comp = this.key.compareTo(this.parent.key);
            return comp < 0;
        }

        public void leftRotate() throws IllegalArgumentException{
            if(this.right == NIL){
                throw new IllegalArgumentException("Node has no right child");
            }
           var right_child = this.right;
           this.setRightChild(right_child.left);

            //Update parent pointer
            if(this.parent == NIL){
                RedBlackTree.this.setRoot(right_child);
            }
            else{
                if(this.isLeftChild()){
                    this.parent.setLeftChild(right_child);
                }
                else{
                    this.parent.setRightChild(right_child);
                }
            }

            right_child.setLeftChild(this);
        }

        public void rightRotate() throws IllegalArgumentException{
            if(this.left == NIL){
                throw new IllegalArgumentException("Node has no left child");
            }
            var left_child = this.left;
            this.setLeftChild(left_child.right);


            //Update parent pointer
            if(this.parent == NIL){ // Root
                RedBlackTree.this.setRoot(left_child);
            }
            else{
                if(this.isLeftChild()){
                    this.parent.setLeftChild(left_child);
                }
                else{
                    this.parent.setRightChild(left_child);
                }
            }
            left_child.setRightChild(this);
        }

        @Override
        public String toString() {
            if(this == NIL){
                return "RBNode{NIL}";
            }
            return "RBNode{" +
                    "key=" + key +
                    ", value=" + value +
                    ", isBlack=" + isBlack +
                    '}';
        }
    }
    private final RBNode NIL;

    private RBNode root;
    public RedBlackTree() {
        NIL = new RBNode(null, null);
        NIL.setIsBlack(true);
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
                current = current.getLeftChild();
            }
            else{
                current = current.getRightChild();
            }
        }
        throw new InvalidKeyException();

    }

    public void setRoot(RBNode node) {
        this.root = node;
        node.parent = NIL; // Only the root node has a parent of NIL
        node.isBlack = true;

    }

    public V retrieve(K key) throws InvalidKeyException {
        var node = find_node(key);
        return node.getValue();

    }

    private void fix(RBNode node){
        if(node.getParent().isBlack() && !node.isBlack()){ // There is no violation, since the node is red
            return;
        }
        RBNode current = node;
        RBNode p = node.getParent();
        while(!p.isBlack()){ // p is red
            var g = p.getParent(); // p is red, so cannot be root, so g exists and is black
            RBNode u;
            if(p.isLeftChild()){ // p is left child of g
                u = g.getRightChild();
                if(u.isBlack()){ // u is a black child of the red g
                    if(!current.isLeftChild()){ // Current is right child of parent, so swap them (since both are red)
                        p.leftRotate(); // Current is now left child of g, and p is a child of current
                        var temp = current;
                        current = p;
                        p = temp;
                        // Fall through to the next case, since now current is left child of p, and both are red
                    }
                    p.setIsBlack(true); // p is black, so loop will terminate
                    g.setIsBlack(false); // g is now red

                    g.rightRotate();
                }
                else{ // u is red and therefore not NIL
                    p.setIsBlack(true);
                    u.setIsBlack(true);
                    g.setIsBlack(false);

                    // Moved problem up to g, so need to fix that

                    current = g;
                    p = g.getParent();
                }
            }
            else{ // p is right child of g
                u = g.getLeftChild();
                if(u.isBlack()){
                    if(current.isLeftChild()){ // Current is left child
                        p.rightRotate(); // Make p the right child of current

                        // Still two red nodes, but now they make a right connection
                        var temp = current;
                        current = p;
                        p = temp;
                    }
                    p.setIsBlack(true); // p is black, so loop will terminate
                    g.setIsBlack(false); // g is now red

                    g.leftRotate();
                }
                else{ // u is red and therefore not NIL
                    p.setIsBlack(true);
                    u.setIsBlack(true);
                    g.setIsBlack(false);

                    current = g;
                    p = g.getParent();
                }

            }
        }
        this.root.setIsBlack(true);

    }

    public void set(K key, V value) {
        var node = new RBNode(key,value);
        if (this.root == NIL){
            this.setRoot(node);
        }
        else{
            var current = this.root;
            RBNode parent = null;
            int comp = 0;
            while(current != NIL){
                if(current.getKey().equals(key)){
                    current.setValue(value);
                    return;
                }
                comp = key.compareTo(current.getKey());
                parent = current;
                if(comp < 0){
                    current = current.getLeftChild();
                }
                else{
                    current = current.getRightChild();
                }
            }

            if(comp < 0){
                parent.setLeftChild(node);
            }
            else{
                parent.setRightChild(node);
            }
            fix(node);
        }
    }
}