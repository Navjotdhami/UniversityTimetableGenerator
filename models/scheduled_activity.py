from dataclasses import dataclass

from models.activity import Activity
from models.time_slot import TimeSlot


@dataclass
class ScheduledActivity:
    """
    Represents one scheduled activity in the final timetable.
    """

    activity: Activity

    timeslot: TimeSlot

    room_id: str