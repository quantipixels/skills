import java.util.HashMap;
import java.util.Locale;
import java.util.Map;

// The project's external-value boundary: canonical writes, aliases, forward compatibility.
interface WireValue {
    String wire();
}

final class WireValues<T extends Enum<T> & WireValue> {
    private final Map<String, T> values = new HashMap<>();
    private final T unknown;

    WireValues(Class<T> type, T unknown) {
        this.unknown = unknown;
        for (T value : type.getEnumConstants()) values.put(value.wire(), value);
    }

    void alias(String token, T value) { values.put(token, value); }
    T read(String token) { return values.getOrDefault(token.toLowerCase(Locale.ROOT), unknown); }
    String write(T value) { return value.wire(); }
}

enum AccountState implements WireValue {
    ENABLED("enabled"), DISABLED("disabled"), UNKNOWN("unknown");
    private final String wire;
    AccountState(String wire) { this.wire = wire; }
    public String wire() { return wire; }
}

final class AccountBoundary {
    static final WireValues<AccountState> values = new WireValues<>(AccountState.class, AccountState.UNKNOWN);
    static { values.alias("live", AccountState.ENABLED); }
    static AccountState read(String token) { return values.read(token); }
    static String write(AccountState value) { return values.write(value); }
}
