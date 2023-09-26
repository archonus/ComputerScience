import java.util.*;

public class LR_AutomatonBuilder {
    Grammar grammar;
    Set<LRAutomatonState> canonicalCollection = new HashSet<>();

    record GotoEntry(LRAutomatonState I, GrammarSymbol X){}

    Map<GotoEntry, LRAutomatonState> gotoTable = new HashMap<>();

    Set<LRItem> getClosure(Set<LRItem> itemSet){
        HashSet<LRItem> result = new HashSet<>(itemSet);
        EnumSet<NonTerminal> added = EnumSet.noneOf(NonTerminal.class);

        boolean cont = false;
        do{
            for (LRItem item: result) {
                var opt_symbol = item.getSymbolAfterPosition();
                if(opt_symbol.isPresent()){
                    var symbol = opt_symbol.get();
                    if(symbol.type() == GrammarSymbol.SymbolType.NONTERMINAL && !added.contains(symbol.nonTerminal())){
                        this.grammar.getProductionsFor(symbol.nonTerminal()).map(LRItem::fromRule).forEach(result::add);
                        added.add(symbol.nonTerminal());
                        cont = true;
                    }
                }
            }
        } while (cont);

        return result;
    }

    void computeGoto(LRAutomatonState state, GrammarSymbol X){
        GotoEntry key = new GotoEntry(state, X);
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

    void computeCanonicalCollection(){
        var startState = new LRAutomatonState(
                getClosure(
                        Set.of(LRItem.fromRule(grammar.rules().get(0)) // First rule should be the start
                        )
                )
        );
        canonicalCollection.add(startState);
        boolean cont = false;
        do{
            int n = canonicalCollection.size();
            for(LRAutomatonState state : canonicalCollection){
                for(Terminal a : Terminal.values()){
                    computeGoto(state, GrammarSymbol.fromTerminal(a));
                }
                for(NonTerminal A : NonTerminal.values()){
                    computeGoto(state, GrammarSymbol.fromNonTerminal(A));
                }

            }
            cont = n != canonicalCollection.size();
        } while(cont);

    }




}
