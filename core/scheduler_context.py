from dataclasses import dataclass, field
from typing import List, Dict

from models.activity import Activity
from models.scheduled_activity import ScheduledActivity
from models.time_slot import TimeSlot
from models.room import Room


@dataclass
class SchedulerContext:
    """
    Central runtime context shared across the scheduling engine.
    Stores input data, generated activities, scheduling state,
    and the final timetable.
    """

    # ---------------------------------------------------------
    # Master Data
    # ---------------------------------------------------------

    courses: List = field(default_factory=list)

    sections: List = field(default_factory=list)

    faculties: List = field(default_factory=list)

    rooms: List[Room] = field(default_factory=list)

    labs: List[Room] = field(default_factory=list)

    # ---------------------------------------------------------
    # Generated Data
    # ---------------------------------------------------------

    timeslots: List[TimeSlot] = field(default_factory=list)

    activities: List[Activity] = field(default_factory=list)

    # ---------------------------------------------------------
    # Scheduler Output
    # ---------------------------------------------------------

    assignments: List[ScheduledActivity] = field(default_factory=list)

    scheduled_classes: List[ScheduledActivity] = field(default_factory=list)

    # ---------------------------------------------------------
    # Runtime Occupancy Maps
    # ---------------------------------------------------------

    faculty_schedule: Dict = field(default_factory=dict)

    room_schedule: Dict = field(default_factory=dict)

    section_schedule: Dict = field(default_factory=dict)