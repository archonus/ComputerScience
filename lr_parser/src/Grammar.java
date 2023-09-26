import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Stream;

public record Grammar(List<GrammarProduction> rules) {
    public Stream<GrammarProduction> getProductionsFor(NonTerminal head){
        return rules.stream().filter(rule -> rule.head().equals(head));
    }
}
