from states import AccountState, LABELS

def dispatch(service, action, key):
    if action == "show":
        row = service.store.get(key)
        return {"id": key, "status": LABELS[AccountState(row["state"])], "cents": row["cents"]}
    raise ValueError("unknown action")
