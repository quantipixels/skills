from enum import Enum

class AccountState(Enum):
    OPEN = "O"
    CLOSED = "C"

LABELS = {AccountState.OPEN: "Open", AccountState.CLOSED: "Closed"}
