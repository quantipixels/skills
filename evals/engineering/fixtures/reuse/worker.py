def run(store, provider):
    for row in store.eligible():
        provider.collect(row["id"], row["cents"])
