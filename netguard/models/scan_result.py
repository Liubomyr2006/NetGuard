

from dataclasses import dataclass
from enum import Enum


class ScanState(str, Enum):
    OPEN = "open"
    CLOSED = "closed"
    FILTERED = "filtered"
    ERROR = "error"


@dataclass(frozen=True, slots=True)
class ScanResult:
    host: str
    port: int
    state: ScanState
    response_time: float | None = None
    error: str | None = None