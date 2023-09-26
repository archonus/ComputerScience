import grammar.Terminal;

import java.io.IOException;
import java.text.ParseException;
import java.util.List;
import java.util.Map;
import java.util.Stack;

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

    void parse(Lexer lexer) throws IOException, LexerException, ParserException {
        Stack<LRAutomatonState> statesStack = new Stack<>();
        statesStack.push(startState);
        Token a = lexer.getNextToken();
        while (true){
            LRAutomatonState currentState = statesStack.peek();
            ShiftReduceAction action = actionTable.get(new ActionEntry(currentState, a.type()));
            if(action == null){
                throw new ParserException("Invalid parse");
            }
            switch (action.actionType()){
                case ACCEPT -> {
                    return;
                }
                case SHIFT -> {
                    //TODO Push token onto stack
                    statesStack.push(states.get(action.index()));
                    a = lexer.getNextToken(); // Consume input
                }
                case REDUCE -> {
                    GrammarProduction production = grammar.rules().get(action.index());
                    for (int i = 0; i < production.bodyLength(); i++) {
                        statesStack.pop();
                        // TODO Pop corresponding tokens stack and use to store
                        var newState = gotoTable.get(
                                new GotoEntry(statesStack.peek(),
                                        GrammarSymbol.fromNonTerminal(production.head()))
                        );
                        statesStack.push(newState);
                        System.out.println(production);
                    }
                }
                case ERROR -> throw new ParserException();
            }
        }
    }
}
