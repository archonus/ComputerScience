public record GrammarSymbol(GrammarSymbol.SymbolType type, Terminal terminal, NonTerminal nonTerminal) {
    public enum SymbolType {TERMINAL, NONTERMINAL}

}
