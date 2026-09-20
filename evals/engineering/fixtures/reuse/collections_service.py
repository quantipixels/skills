from states import AccountState

class Collections:
    def __init__(self, store): self.store = store
    def hold(self, key):
        if self.store.get(key)["state"] != AccountState.OPEN.value:
            raise ValueError("closed account")
        self.store.suspend(key, True)
    def release(self, key):
        if self.store.get(key)["state"] != AccountState.OPEN.value:
            raise ValueError("closed account")
        self.store.suspend(key, False)
