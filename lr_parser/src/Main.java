import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException, LexerException {
        System.out.println("Hello world!");
//        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
//        Lexer l = new Lexer(reader);
//        Token t = l.getNextToken();
//        while(!t.equals(Token.End)){
//            System.out.println(t);
//            t = l.getNextToken();
//        }
        var builder = new LR_AutomatonBuilder();
        builder.grammar = new ParserGrammar();
        builder.computeCanonicalCollection();
        for(var state : builder.states){
            System.out.println(state);
        }
        builder.computeTables();
        System.out.println(builder.actionTable);

    }
}