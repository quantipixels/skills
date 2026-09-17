"""Executable Java boundary probes and controls; no model calls or performance claims."""
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

FIXTURE = Path(__file__).with_name("fixtures") / "domain-values"
PROBES = {
    "positive": '''
        DeliveryState paused = Enum.valueOf(DeliveryState.class, "PAUSED");
        eq("paused", DeliveryBoundary.write(paused));
        eq(paused, DeliveryBoundary.read("paused"));
        eq(paused, DeliveryBoundary.read("HOLD"));
        DeliveryBoundary.values.alias("operator-pause", paused);
        eq(paused, DeliveryBoundary.read("operator-pause"));
        eq(DeliveryState.QUEUED, DeliveryBoundary.read("pending"));
        eq("queued", DeliveryBoundary.write(DeliveryState.QUEUED));
        eq(DeliveryState.ACTIVE, DeliveryBoundary.read("ACTIVE"));
        eq(DeliveryState.UNKNOWN, DeliveryBoundary.read("future-state"));
    ''',
    "negative": '''
        LayoutMode compact = Enum.valueOf(LayoutMode.class, "COMPACT");
        eq(compact, LayoutChoice.read("compact"));
        eq("compact", LayoutChoice.write(compact));
        eq(LayoutMode.COMFORTABLE, LayoutChoice.read("comfortable"));
        eq("comfortable", LayoutChoice.write(LayoutMode.COMFORTABLE));
        for (String value : new String[]{"COMPACT", " compact", "compact ", "dense", "future"}) {
            boolean rejected = false;
            try { LayoutChoice.read(value); }
            catch (IllegalArgumentException expected) { rejected = true; }
            if (!rejected) throw new AssertionError("accepted invalid internal token: " + value);
        }
    ''',
}


def probe(workspace, case):
    """Compile errors propagate; behavioral rejection has a distinct failed result."""
    if case not in PROBES:
        raise ValueError(f"unknown case: {case}")
    with tempfile.TemporaryDirectory(prefix="qp-java-oracle-") as directory:
        root = Path(directory)
        source = "DeliveryBoundary.java" if case == "positive" else "LayoutChoice.java"
        for name in ("WireValues.java", source):
            shutil.copy2(Path(workspace) / name, root / name)
        (root / "BoundaryProbe.java").write_text('''
class BoundaryProbe {
    static void eq(Object expected, Object actual) {
        if (!expected.equals(actual)) throw new AssertionError(expected + " != " + actual);
    }
    public static void main(String[] args) {
        eq(AccountState.ENABLED, AccountBoundary.read("LIVE"));
        eq("enabled", AccountBoundary.write(AccountState.ENABLED));
        eq(AccountState.UNKNOWN, AccountBoundary.read("future"));
''' + PROBES[case] + "\n    }\n}\n")
        subprocess.run(["javac", "-d", str(root), *map(str, root.glob("*.java"))],
                       capture_output=True, text=True, check=True, timeout=15)
        result = subprocess.run(["java", "-cp", str(root), "BoundaryProbe"],
                                capture_output=True, text=True, timeout=15)
        if result.returncode == 0:
            return {"status": "passed", "case": case}
        # Missing enum constants are the original feature gap. Other runtime errors
        # stay errors; compiler failures never become behavioral rejection.
        expected = ("java.lang.AssertionError", "No enum constant DeliveryState.PAUSED",
                    "No enum constant LayoutMode.COMPACT")
        return {"status": "failed" if any(x in result.stderr for x in expected) else "error",
                "case": case, "detail": result.stderr}


POSITIVE_GOOD = '''
enum DeliveryState implements WireValue {
    QUEUED("queued"), ACTIVE("active"), PAUSED("paused"), UNKNOWN("unknown");
    private final String wire;
    DeliveryState(String wire) { this.wire = wire; }
    public String wire() { return wire; }
}
final class DeliveryBoundary {
    static final WireValues<DeliveryState> values = new WireValues<>(DeliveryState.class, DeliveryState.UNKNOWN);
    static { values.alias("pending", DeliveryState.QUEUED); values.alias("hold", DeliveryState.PAUSED); }
    static DeliveryState read(String token) { return values.read(token); }
    static String write(DeliveryState value) { return values.write(value); }
}
'''
NEGATIVE_GOOD = '''
enum LayoutMode { COMFORTABLE, COMPACT }
final class LayoutChoice {
    static LayoutMode read(String token) {
        return switch (token) {
            case "comfortable" -> LayoutMode.COMFORTABLE;
            case "compact" -> LayoutMode.COMPACT;
            default -> throw new IllegalArgumentException("invalid layout");
        };
    }
    static String write(LayoutMode value) {
        return switch (value) { case COMFORTABLE -> "comfortable"; case COMPACT -> "compact"; };
    }
}
'''
NEGATIVE_BAD = '''
enum LayoutMode implements WireValue {
    COMFORTABLE, COMPACT;
    public String wire() { return name().toLowerCase(java.util.Locale.ROOT); }
}
final class LayoutChoice {
    static final WireValues<LayoutMode> values = new WireValues<>(LayoutMode.class, LayoutMode.COMFORTABLE);
    static LayoutMode read(String token) { return values.read(token); }
    static String write(LayoutMode value) { return values.write(value); }
}
'''


class DomainValueOracleTest(unittest.TestCase):
    def workspace(self, root, case, candidate=None):
        shutil.copy2(FIXTURE / "WireValues.java", root / "WireValues.java")
        name = "DeliveryBoundary.java" if case == "positive" else "LayoutChoice.java"
        shutil.copy2(FIXTURE / case / name, root / name)
        if candidate is not None:
            (root / name).write_text(candidate)
        return root

    def test_originals_fail_for_missing_value(self):
        for case in PROBES:
            with self.subTest(case=case), tempfile.TemporaryDirectory() as temp:
                self.assertEqual("failed", probe(self.workspace(Path(temp), case), case)["status"])

    def test_correct_seam_and_deliberate_nonreuse_pass(self):
        for case, candidate in (("positive", POSITIVE_GOOD), ("negative", NEGATIVE_GOOD)):
            with self.subTest(case=case), tempfile.TemporaryDirectory() as temp:
                self.assertEqual("passed", probe(self.workspace(Path(temp), case, candidate), case)["status"])

    def test_ad_hoc_parser_rejects_dynamic_alias(self):
        candidate = POSITIVE_GOOD.replace("return values.read(token);", '''
            return switch (token.toLowerCase(java.util.Locale.ROOT)) {
                case "paused", "hold" -> DeliveryState.PAUSED;
                case "pending", "queued" -> DeliveryState.QUEUED;
                case "active" -> DeliveryState.ACTIVE;
                default -> DeliveryState.UNKNOWN;
            };''')
        with tempfile.TemporaryDirectory() as temp:
            result = probe(self.workspace(Path(temp), "positive", candidate), "positive")
            self.assertEqual("failed", result["status"])
            self.assertIn("PAUSED != UNKNOWN", result["detail"])

    def test_cargo_cult_converter_rejected_at_internal_boundary(self):
        with tempfile.TemporaryDirectory() as temp:
            result = probe(self.workspace(Path(temp), "negative", NEGATIVE_BAD), "negative")
            self.assertEqual("failed", result["status"])
            self.assertIn("accepted invalid internal token: COMPACT", result["detail"])

    def test_compile_error_is_not_behavioral_failure(self):
        with tempfile.TemporaryDirectory() as temp:
            root = self.workspace(Path(temp), "positive", "not Java")
            with self.assertRaises(subprocess.CalledProcessError):
                probe(root, "positive")


if __name__ == "__main__":
    unittest.main()
