import java.util.List;

public record GrammarProduction(NonTerminal head, List<GrammarSymbol> body) {
    public int bodyLength() {return body.size();}
}
