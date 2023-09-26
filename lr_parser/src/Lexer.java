import java.io.IOException;
import java.io.Reader;

public class Lexer {
    Reader reader;

    public Lexer(Reader reader) {
        this.reader = reader;
    }

    private Character getNextCharacter() throws IOException {
        var i = reader.read();
        if (i == -1) {
            return null;
        }
        return (char) i;
    }

    public Token getNextToken() throws IOException, LexerException {
        Character current_char;

        do { // Skip whitespace and return if end of input reached
            current_char = getNextCharacter();
            if (current_char == null) {
                return Token.End;
            }
        }
        while (Character.isWhitespace(current_char));

        StringBuilder lexemeBuilder = new StringBuilder();

        switch (current_char) { // Match against simple terminals
            case '!' -> {
                return Token.Factorial;
            }
            case '(' -> {
                return Token.OpenBracket;
            }
            case ')' -> {
                return Token.CloseBracket;
            }
            case '+' -> {
                return Token.Plus;
            }
            case '*' -> {
                return Token.Times;
            }
            case '-' -> {
                return Token.Minus;
            }
            case 'c', 'C' -> {
                if (
                        Character.toLowerCase(getNextCharacter()) == 'o' &&
                                Character.toLowerCase(getNextCharacter()) == 's'
                ) {
                    return Token.Cos;
                }
                else {
                    throw new LexerException("Invalid lexeme");
                }
            }
        }

        if (!Character.isDigit(current_char)) { // Match against digit
            throw new LexerException("Invalid character " + current_char);
        }
        do {
            lexemeBuilder.append(current_char);
            Character c = getNextCharacter();
            if (c == null) {
                return new Token(Terminal.NUMBER, lexemeBuilder.toString());
            }
            current_char = c;
        } while (Character.isDigit(current_char));
        if (current_char != '.') {
            return new Token(Terminal.NUMBER, lexemeBuilder.toString());
        }
        else { // Repeat for after decimal point
            do {
                lexemeBuilder.append(current_char);
                Character c = getNextCharacter();
                if (c == null) {
                    return new Token(Terminal.NUMBER, lexemeBuilder.toString());
                }
                current_char = c;
            } while (Character.isDigit(current_char));
            return new Token(Terminal.NUMBER, lexemeBuilder.toString());
        }
    }

}
