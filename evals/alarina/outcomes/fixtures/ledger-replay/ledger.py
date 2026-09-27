def record(entries, event_id, amount):
    if event_id in entries:
        return sum(entries.values())
    entries[event_id] = amount
    return sum(entries.values())
