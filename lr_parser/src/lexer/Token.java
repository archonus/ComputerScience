package lexer;

import grammar.Terminal;

public record Token(Terminal type, String lexeme) {
    public static Token End = new Token(Terminal.END, "");
    public static Token Factorial = new Token(Terminal.FACTORIAL, "!");
    public static Token Cos = new Token(Terminal.COS, "cos");

    public static Token Plus = new Token(Terminal.PLUS, "+");

    public static Token Minus = new Token(Terminal.MINUS, "-");
    public static Token Times = new Token(Terminal.TIMES, "*");

    public static Token OpenBracket = new Token(Terminal.OPEN_BRACKET,"(");
    public static Token CloseBracket = new Token(Terminal.CLOSE_BRACKET, ")");

}
