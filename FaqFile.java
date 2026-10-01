import java.util.regex.Pattern;

/**
 * Reads and writes the "question=answer" lines in faq.txt. A '=' or '\' inside a
 * question is saved with a backslash in front so it can't be mistaken for the
 * separator; lines saved before this change have no backslashes and load the same.
 */
final class FaqFile {
    // The codes a terminal sends for keys like the arrows, e.g. ESC [ A.
    private static final Pattern ESCAPE_SEQUENCE = Pattern.compile("\\x1B(\\[[0-9;?]*[ -/]*[@-~]|O.)");

    private FaqFile() {}

    static String formatLine(String question, String answer) {
        return question.replace("\\", "\\\\").replace("=", "\\=") + "=" + answer;
    }

    /** Returns {question, answer}, or null when the line has no separator. */
    static String[] parseLine(String line) {
        StringBuilder question = new StringBuilder();
        for (int i = 0; i < line.length(); i++) {
            char c = line.charAt(i);
            if (c == '\\' && i + 1 < line.length()) {
                question.append(line.charAt(++i));
            } else if (c == '=') {
                return new String[] { question.toString(), line.substring(i + 1) };
            } else {
                question.append(c);
            }
        }
        return null;
    }

    /** Removes key escape codes and other control characters, then trims. */
    static String clean(String text) {
        return ESCAPE_SEQUENCE.matcher(text).replaceAll("").replaceAll("\\p{Cntrl}", "").trim();
    }
}
