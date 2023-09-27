package parser;

import grammar.Grammar;
import grammar.GrammarProduction;
import grammar.GrammarSymbol;
import grammar.Terminal;
import lexer.Lexer;
import lexer.LexerException;
import lexer.Token;

import java.io.IOException;
import java.util.*;

public class LRParser {
    record GotoEntry(LRAutomatonState I, GrammarSymbol X){}

    record ActionEntry(LRAutomatonState I, Terminal a){}

    Grammar grammar;
    List<LRAutomatonState> states;

    LRAutomatonState startState;

    Map<GotoEntry, LRAutomatonState> gotoTable;

    Map<ActionEntry, ShiftReduceAction> actionTable;

    LRParser(Grammar grammar,
             List<LRAutomatonState> states,
             LRAutomatonState startState,
             Map<GotoEntry, LRAutomatonState> gotoTable,
             Map<ActionEntry, ShiftReduceAction> actionTable) {
        this.grammar = grammar;
        this.states = states;
        this.startState = startState;
        this.gotoTable = gotoTable;
        this.actionTable = actionTable;
    }

    public ParseTreeNode parse(Lexer lexer) throws IOException, LexerException, ParserException {
        Deque<LRAutomatonState> statesStack = new ArrayDeque<>();
        Deque<ParseTreeNode> nodesStack = new ArrayDeque<>();
        statesStack.push(startState);
        Token token = lexer.getNextToken();
        System.out.println(token);
        while (true){
            LRAutomatonState currentState = statesStack.peek();
            ShiftReduceAction action = actionTable.get(new ActionEntry(currentState, token.type()));
            if(action == null){
                throw new ParserException("Syntax error: unexpected token " + token.lexeme());
            }
            switch (action.actionType()){
                case ACCEPT -> {
                    // Assert that stack length == 1
                    return nodesStack.pop();
                }
                case SHIFT -> {
                    nodesStack.push(ParseTreeNode.createParseTreeNode(token));
                    statesStack.push(states.get(action.index())); // Push next state onto stack
                    token = lexer.getNextToken(); // Consume input
                    System.out.println(token);
                }
                case REDUCE -> {
                    GrammarProduction production = grammar.rules().get(action.index());
                    // Using a stack reverses the order of the children
                    Deque<ParseTreeNode> children = new ArrayDeque<>(production.bodyLength());
                    for (int i = 0; i < production.bodyLength(); i++) {
                        statesStack.pop();
                        children.push(nodesStack.pop());
                    }
                    var newState = gotoTable.get(
                            new GotoEntry(statesStack.peek(),
                                    GrammarSymbol.fromNonTerminal(production.head()))
                    );
                    statesStack.push(newState);
                    nodesStack.push(ParseTreeNode.createParseTreeNode(production.head(), children));
                    System.out.println(production);
                }
                case ERROR -> throw new ParserException();
            }
        }
    }
}
