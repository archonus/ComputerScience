import grammar.ParserGrammar;
import lexer.Lexer;
import lexer.LexerException;
import parser.LR_AutomatonBuilder;
import parser.ParserException;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException, LexerException, ParserException {
        System.out.println("Hello world!");
        BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
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
        builder.buildParser().parse(l);


    }
}