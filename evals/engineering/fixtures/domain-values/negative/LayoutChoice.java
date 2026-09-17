enum LayoutMode { COMFORTABLE }

// Internal preference boundary: exact tokens; invalid input is a caller error.
final class LayoutChoice {
    static LayoutMode read(String token) {
        if ("comfortable".equals(token)) return LayoutMode.COMFORTABLE;
        throw new IllegalArgumentException("invalid layout");
    }
    static String write(LayoutMode mode) { return "comfortable"; }
}
