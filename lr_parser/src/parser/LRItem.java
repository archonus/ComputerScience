package parser;

import grammar.GrammarProduction;
import grammar.GrammarSymbol;

import java.util.Optional;

public record LRItem(GrammarProduction production, int position) {
    public static LRItem fromRule(GrammarProduction production){
        return new LRItem(production, 0);
    }
    public Optional<GrammarSymbol> getSymbolAfterPosition(){
        if(position == production().bodyLength()){
            return Optional.empty();
        }
        return Optional.of(production.body().get(position));
    }

}
