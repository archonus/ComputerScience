package grammar;

import java.util.*;

import static grammar.NonTerminal.*;
import static grammar.Terminal.*;

public class ParserGrammar extends Grammar {
    Map<NonTerminal, Set<Terminal>> firsts = new EnumMap<>(NonTerminal.class);
    Map<NonTerminal, Set<Terminal>> follows = new EnumMap<>(NonTerminal.class);

    public ParserGrammar() {
        this(List.of(
                // E' -> E
                new GrammarProduction(STATEMENT, List.of(GrammarSymbol.fromNonTerminal(E))),
                // E -> S
                new GrammarProduction(E, List.of(GrammarSymbol.fromNonTerminal(S))),
                // E -> E + S
                new GrammarProduction(E,
                        List.of(GrammarSymbol.fromNonTerminal(E),
                                GrammarSymbol.fromTerminal(PLUS),
                                GrammarSymbol.fromNonTerminal(S))),
                // S -> M
                new GrammarProduction(S, List.of(GrammarSymbol.fromNonTerminal(M))),
                //S -> S - M
                new GrammarProduction(S,
                        List.of(GrammarSymbol.fromNonTerminal(S),
                                GrammarSymbol.fromTerminal(MINUS),
                                GrammarSymbol.fromNonTerminal(M))),
                // M -> C * M
                new GrammarProduction(M,
                        List.of(GrammarSymbol.fromNonTerminal(C),
                                GrammarSymbol.fromTerminal(TIMES),
                                GrammarSymbol.fromNonTerminal(M))),
                // M -> C
                new GrammarProduction(M,
                        List.of(GrammarSymbol.fromNonTerminal(C))),
                // C -> cos C
                new GrammarProduction(C,
                        List.of(GrammarSymbol.fromTerminal(COS),
                                GrammarSymbol.fromNonTerminal(C))),
                // C -> F
                new GrammarProduction(C, List.of(GrammarSymbol.fromNonTerminal(F))),
                //F -> num
                new GrammarProduction(F, List.of(GrammarSymbol.fromTerminal(NUMBER))),
                // F -> - num
                new GrammarProduction(F,
                        List.of(GrammarSymbol.fromTerminal(MINUS),
                                GrammarSymbol.fromTerminal(NUMBER))),
                // F -> F!
                new GrammarProduction(F,
                        List.of(GrammarSymbol.fromNonTerminal(F),
                                GrammarSymbol.fromTerminal(FACTORIAL))),
                // F -> (E)
                new GrammarProduction(F,
                        List.of(GrammarSymbol.fromTerminal(OPEN_BRACKET),
                                GrammarSymbol.fromNonTerminal(E),
                                GrammarSymbol.fromTerminal(CLOSE_BRACKET)))
        ));

    }


    ParserGrammar(List<GrammarProduction> rules) {
        super(rules);
        var commonFirst = EnumSet.of(NUMBER, MINUS, OPEN_BRACKET, COS);
        for (NonTerminal A : NonTerminal.values()) {
            firsts.put(A, commonFirst);
        }
        firsts.put(F, EnumSet.of(NUMBER, MINUS, OPEN_BRACKET)); // Excluding cos

        follows.put(STATEMENT, Set.of(END));

        follows.put(E, Set.of(END, CLOSE_BRACKET, PLUS));

        follows.put(S, Set.of(END, CLOSE_BRACKET, PLUS, MINUS));

        follows.put(M, Set.of(END, CLOSE_BRACKET, PLUS, MINUS));
        follows.put(C, Set.of(END,
                CLOSE_BRACKET,
                PLUS,
                MINUS,
                TIMES));

        follows.put(F, Set.of(END,
                CLOSE_BRACKET,
                PLUS,
                MINUS,
                TIMES,
                FACTORIAL));
    }

    @Override
    public Set<Terminal> first(NonTerminal A) {
        return firsts.get(A);
    }

    @Override
    public Set<Terminal> follow(NonTerminal A) {
        return follows.get(A);
    }
}
