package grammar;

import java.util.*;
import java.util.stream.Stream;

public abstract class Grammar {
    private final List<GrammarProduction> rules;

    public Grammar(List<GrammarProduction> rules) {
        this.rules = rules;
    }

    public Stream<GrammarProduction> getProductionsFor(NonTerminal head) {
        return rules.stream().filter(rule -> rule.head().equals(head));
    }

    public List<GrammarProduction> rules() {
        return rules;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == this) return true;
        if (obj == null || obj.getClass() != this.getClass()) return false;
        var that = (Grammar) obj;
        return Objects.equals(this.rules, that.rules);
    }

    @Override
    public int hashCode() {
        return Objects.hash(rules);
    }

    @Override
    public String toString() {
        return "grammar.Grammar[" +
                "rules=" + rules + ']';
    }

    public abstract Set<Terminal> first(NonTerminal A);

    public abstract Set<Terminal> follow(NonTerminal A);

}

