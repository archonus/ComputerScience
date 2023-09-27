package parser;

import grammar.GrammarSymbol;
import grammar.NonTerminal;
import lexer.Token;

import java.util.Collection;
import java.util.Collections;
import java.util.List;
import java.util.stream.Stream;


public class ParseTreeNode {
    final GrammarSymbol symbol;
    final Token token;

    private final Collection<ParseTreeNode> children;

    private ParseTreeNode(GrammarSymbol symbol,  Collection<ParseTreeNode> children) {
        this.token = null;
        this.symbol = symbol;
        this.children = children;
    }

    private ParseTreeNode(GrammarSymbol symbol, Token token, Collection<ParseTreeNode> children){
        this.token = token;
        this.symbol = GrammarSymbol.fromTerminal(token.type());
        this.children = Collections.emptyList();
    }

    public static ParseTreeNode createParseTreeNode(Token token) {
        return new ParseTreeNode(
                GrammarSymbol.fromTerminal(token.type()),
                token,
                Collections.emptyList()
        );
    }

    public static ParseTreeNode createParseTreeNode(NonTerminal A, Collection<ParseTreeNode> children) {
        return new ParseTreeNode(
                GrammarSymbol.fromNonTerminal(A),
                children
        );
    }
    public static ParseTreeNode createParseTreeNode(NonTerminal A, ParseTreeNode... children) {
        return new ParseTreeNode(
                GrammarSymbol.fromNonTerminal(A),
                List.of(children)
        );
    }

    public boolean isLeaf(){
        return token != null;
    }

    public Stream<ParseTreeNode> getChildren(){
        return children.stream();
    }

    @Override
    public String toString() {
        return "ParseTreeNode{" +
                "symbol=" + symbol +
                ", children=" + children +
                '}';
    }
}
