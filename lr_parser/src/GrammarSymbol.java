import grammar.NonTerminal;
import grammar.Terminal;

public record GrammarSymbol(GrammarSymbol.SymbolType type, Terminal terminal, NonTerminal nonTerminal) {
    public enum SymbolType {TERMINAL, NONTERMINAL}

    public static GrammarSymbol fromTerminal(Terminal t){
        return new GrammarSymbol(SymbolType.TERMINAL, t, null);
    }

    public static GrammarSymbol fromNonTerminal(NonTerminal A){
        return new GrammarSymbol(SymbolType.NONTERMINAL, null,A);
    }

    @Override
    public String toString() {
        return switch (type){

            case TERMINAL -> terminal.toString();
            case NONTERMINAL -> nonTerminal.toString();
        };
    }
}
