import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Stream;

public class Grammar {
    public Set<GrammarProduction> rules;

    public Grammar(Set<GrammarProduction> rules) {
        this.rules = rules;
    }

    public Grammar(GrammarProduction... rules){
        this(List.of(rules));
    }

    public Grammar(List<GrammarProduction> rules){
        this.rules = new HashSet<>(rules.size());
        this.rules.addAll(rules);
    }

    public Stream<GrammarProduction> getProductionsFor(NonTerminal head){
        return rules.stream().filter(rule -> rule.head().equals(head));
    }
}
