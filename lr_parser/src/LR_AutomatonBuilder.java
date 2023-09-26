import java.util.EnumSet;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class LR_AutomatonBuilder {
    Grammar grammar;
    List<LRAutomatonState> canonicalCollection;

    record GotoEntry(LRAutomatonState I, GrammarSymbol X){}
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




}
