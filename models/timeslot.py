from dataclasses import dataclass


@dataclass(frozen=True)
class TimeSlot:

    day: str

    period: int