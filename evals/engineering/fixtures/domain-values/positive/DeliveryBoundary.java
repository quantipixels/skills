enum DeliveryState implements WireValue {
    QUEUED("queued"), ACTIVE("active"), UNKNOWN("unknown");
    private final String wire;
    DeliveryState(String wire) { this.wire = wire; }
    public String wire() { return wire; }
}

final class DeliveryBoundary {
    static final WireValues<DeliveryState> values = new WireValues<>(DeliveryState.class, DeliveryState.UNKNOWN);
    static { values.alias("pending", DeliveryState.QUEUED); }
    static DeliveryState read(String token) { return values.read(token); }
    static String write(DeliveryState value) { return values.write(value); }
}
