import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        lcsMain();
    }

    public static void lcsMain() throws IOException{
        var br = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter first string...");
        var xs = br.readLine();
        System.out.print("Enter second string...");
        var ys = br.readLine();
        var s= LCS.longestCommonSubsequence(xs,ys);
        System.out.println(s);
    }
}