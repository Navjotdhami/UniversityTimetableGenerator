from dataclasses import dataclass


@dataclass(frozen=True)
class TimeSlot:

    day: str

    shift: int

    period: int

    start_time: str

    end_time: str