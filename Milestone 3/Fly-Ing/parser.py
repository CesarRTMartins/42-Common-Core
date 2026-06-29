from dataclasses import dataclass, field
from enum import Enum


class ZoneType(Enum):
    NORMAL = "normal"
    BLOCKED = "blocked"
    RESTRICTED = "restricted"
    PRIORITY = "priority"

    @property
    def movement_cost(self) -> int:
        """Turns required to move INTO a zone of this type."""
        return 2 if self is ZoneType.RESTRICTED else 1

    @property
    def is_accessible(self) -> bool:
        return self is not ZoneType.BLOCKED


@dataclass
class Zone:
    name: str
    x: int
    y: int
    zone_type: ZoneType = ZoneType.NORMAL
    color: str | None = None
    max_drones: int = 1
    is_start: bool = False
    is_end: bool = False

    def current_capacity(self, occupants: int) -> int:
        """Remaining free slots given a current occupant count.

        Start/end zones are unlimited, so this only really matters
        for normal/restricted/priority zones with finite max_drones.
        """
        if self.is_start or self.is_end:
            return float("inf")  # type: ignore[return-value]
        return self.max_drones - occupants

    def __repr__(self) -> str:
        return f"Zone({self.name!r}, type={self.zone_type.value})"

class movements()