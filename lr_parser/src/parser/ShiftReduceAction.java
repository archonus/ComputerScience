package parser;

public record ShiftReduceAction(ActionType actionType, int index) {
    public enum ActionType{SHIFT, REDUCE, ACCEPT, ERROR}
    public static ShiftReduceAction Accept = new ShiftReduceAction(ActionType.ACCEPT, -1);
    public static ShiftReduceAction Error = new ShiftReduceAction(ActionType.ERROR, -1);
}
