import grammar.NonTerminal;
import grammar.Terminal;

import java.util.*;

public class LR_AutomatonBuilder {
    public LR_AutomatonBuilder(Grammar grammar) {
        this.grammar = grammar;
    }

    Grammar grammar;
    private final Set<LRAutomatonState> canonicalCollection = new HashSet<>();

    List<LRAutomatonState> states;

    LRAutomatonState startState;

    Map<LRParser.ActionEntry, ShiftReduceAction> actionTable = new HashMap<>();

    Map<LRParser.GotoEntry, LRAutomatonState> gotoTable = new HashMap<>();

    Set<LRItem> getClosure(Set<LRItem> itemSet){
        HashSet<LRItem> result = new HashSet<>(itemSet);
        EnumSet<NonTerminal> added = EnumSet.noneOf(NonTerminal.class);

        boolean cont = false;
        do{
            cont = false;
            List<LRItem> itemsToAdd = new ArrayList<>(); // Prevent modification while iteration
            for (LRItem item: result) {
                var opt_symbol = item.getSymbolAfterPosition();
                if(opt_symbol.isPresent()){
                    var symbol = opt_symbol.get();
                    if(symbol.type() == GrammarSymbol.SymbolType.NONTERMINAL && !added.contains(symbol.nonTerminal())){
                        this.grammar.getProductionsFor(symbol.nonTerminal()).map(LRItem::fromRule).forEach(itemsToAdd::add);
                        added.add(symbol.nonTerminal());
                        cont = true;
                    }
                }
            }
            result.addAll(itemsToAdd);
        } while (cont);

        return result;
    }

    void computeGoto(LRAutomatonState state, GrammarSymbol X){
        LRParser.GotoEntry key = new LRParser.GotoEntry(state, X);
        var result = gotoTable.get(key);
        if (result == null) { // Not been processed
            Set<LRItem> immediateTransition = new HashSet<>();
            for(LRItem item : state.items()){
                var opt_symbol = item.getSymbolAfterPosition();
                if(opt_symbol.isPresent() && opt_symbol.get().equals(X)){
                    immediateTransition.add(new LRItem(item.production(), item.position() + 1));
                }
            }
            var newState = new LRAutomatonState(getClosure(immediateTransition));
            canonicalCollection.add(newState);
            gotoTable.put(key, newState);
        }
    }

    void computeTables(){
        for(LRAutomatonState state : states){ // For each state
            for(LRItem item : state.items()){ // For each item in the state
                var opt_symbol = item.getSymbolAfterPosition();
                if(opt_symbol.isPresent()){
                    GrammarSymbol symbol = opt_symbol.get();
                    if(symbol.type() == GrammarSymbol.SymbolType.TERMINAL){
                        var nextState = Objects.requireNonNull(gotoTable.get(new LRParser.GotoEntry(state, symbol)));
                        actionTable.putIfAbsent(new LRParser.ActionEntry(state, symbol.terminal()),
                                new ShiftReduceAction(ShiftReduceAction.ActionType.SHIFT, states.indexOf(nextState)));
                    }
                }
                else { // Position at end
                    NonTerminal head = item.production().head();
                    if(head != NonTerminal.STATEMENT){
                        for(Terminal a : grammar.follow(head)){
                            actionTable.putIfAbsent(
                                    new LRParser.ActionEntry(state, a),
                                    new ShiftReduceAction(ShiftReduceAction.ActionType.REDUCE,
                                            grammar.rules().indexOf(item.production()))
                            );
                        }
                    }
                    else{
                        if(item.position() == item.production().bodyLength()){
                            actionTable.putIfAbsent(
                                    new LRParser.ActionEntry(state, Terminal.END),
                                    ShiftReduceAction.Accept
                            );
                        }
                    }
                }
            }
        }

    }

    void computeCanonicalCollection(){
        startState = new LRAutomatonState(
                getClosure(
                        Set.of(LRItem.fromRule(grammar.rules().get(0)) // First rule should be the start
                        )
                )
        );
        canonicalCollection.add(startState);
        boolean cont = false;
        do{
            int n = canonicalCollection.size();
            LRAutomatonState[] states = canonicalCollection.toArray(new LRAutomatonState[0]);
            for (int i = 0; i < n; i++) {
                LRAutomatonState state = states[i];
                for (Terminal a : Terminal.values()) {
                    computeGoto(state, GrammarSymbol.fromTerminal(a));
                }
                for (NonTerminal A : NonTerminal.values()) {
                    computeGoto(state, GrammarSymbol.fromNonTerminal(A));
                }

            }
            cont = n != canonicalCollection.size();
        } while(cont);
        states = List.of(canonicalCollection.toArray(new LRAutomatonState[0]));
    }

    public LRParser buildParser(){
        computeCanonicalCollection();
        computeTables();
        return new LRParser(grammar, states, startState, gotoTable, actionTable);
    }




}
