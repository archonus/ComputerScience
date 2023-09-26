package grammar;

import java.util.List;

public record GrammarProduction(NonTerminal head, List<GrammarSymbol> body) {
    public int bodyLength() {return body.size();}

    @Override
    public String toString() {
        return "grammar.GrammarProduction{" +
                head +
                " -> " + body +
                '}';
    }
}
