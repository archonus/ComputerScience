package parser;

import java.util.Set;

public record LRAutomatonState(Set<LRItem> items) {
    public boolean isEmpty(){
        return items.isEmpty();
    }
}
