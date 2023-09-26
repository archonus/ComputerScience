public record GrammarSymbol(GrammarSymbol.SymbolType type, Terminal terminal, NonTerminal nonTerminal) {
    public enum SymbolType {TERMINAL, NONTERMINAL}

    public static GrammarSymbol fromTerminal(Terminal t){
        return new GrammarSymbol(SymbolType.TERMINAL, t, null);
    }

    public static GrammarSymbol fromNonTerminal(NonTerminal A){
        return new GrammarSymbol(SymbolType.NONTERMINAL, null,A);
    }

}
