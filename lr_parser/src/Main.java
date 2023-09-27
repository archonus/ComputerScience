import grammar.ParserGrammar;
import lexer.Lexer;
import lexer.LexerException;
import parser.LR_AutomatonBuilder;
import parser.ParserException;

import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException, LexerException, ParserException {
        System.out.println("Hello world!");
        Reader reader;
        if(args.length == 0){
            reader = new BufferedReader(new FileReader("input.txt"));
        }
        else{
            reader = new StringReader(args[0]);
        }
        Lexer l = new Lexer(reader);
//        lexer.Token t = l.getNextToken();
//        while(!t.equals(lexer.Token.End)){
//            System.out.println(t);
//            t = l.getNextToken();
//        }
        var builder = new LR_AutomatonBuilder(new ParserGrammar());
//        builder.computeCanonicalCollection();
//        for(var state : builder.states){
//            System.out.println(state);
//        }
//        builder.computeTables();
//        System.out.print("Start state: " + builder.states.indexOf(builder.startState));
//        System.out.println(builder.startState);
//        System.out.println(builder.actionTable);
        var tree = builder.buildParser().parse(l);
        System.out.println(tree);


    }
}