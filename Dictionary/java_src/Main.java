public class Main {

    public static void main(String[] args) {
        System.out.println("Hello");
        var rbt = new RedBlackTree<Integer,String>();
        var n = 50;
        for (Integer i = n; i >= 0; i--) {
            rbt.set(i,i.toString());
        }
        try {
            System.out.println((rbt.retrieve(24)));
            System.out.println(rbt.retrieve(3));
        }
        catch (InvalidKeyException e){
            System.out.println("Invalid key exception thrown");
        }
    }
}
