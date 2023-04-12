public class RBNode<K,V> {
    private K key;
    private V value;
    private boolean isBlack;

    private RBNode<K,V> left;
    private  RBNode<K,V> right;

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

    public RBNode<K, V> getLeft() {
        return left;
    }

    public void setLeft(RBNode<K, V> left) {
        this.left = left;
    }

    public RBNode<K, V> getRight() {
        return right;
    }

    public void setRight(RBNode<K, V> right) {
        this.right = right;
    }
}
