package grammar;

import java.util.List;
import java.util.Set;

import static grammar.NonTerminal.*;
import static grammar.Terminal.*;

public class TestGrammar extends Grammar {

    public TestGrammar() {
        super(List.of(
                new GrammarProduction(STATEMENT, List.of(GrammarSymbol.fromNonTerminal(E))),
                new GrammarProduction(E, List.of(GrammarSymbol.fromNonTerminal(S))),
                new GrammarProduction(E,
                        List.of(GrammarSymbol.fromNonTerminal(E),
                                GrammarSymbol.fromTerminal(PLUS),
                                GrammarSymbol.fromNonTerminal(S))),
                new GrammarProduction(S, List.of(GrammarSymbol.fromTerminal(NUMBER)))
        ));
    }

    @Override
    public Set<Terminal> first(NonTerminal A) {
        return switch (A) {

            case F, M, C -> Set.of();
            case S, E, STATEMENT -> Set.of(NUMBER);
        };
    }

    @Override
    public Set<Terminal> follow(NonTerminal A) {
        return switch (A) {
            case STATEMENT -> Set.of(END);
            case E, S -> Set.of(PLUS, END);
            default -> Set.of();
        };
    }
}
