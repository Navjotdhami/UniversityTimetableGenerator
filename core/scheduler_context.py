from dataclasses import dataclass, field


@dataclass
class SchedulerContext:
    # Master Data
    courses: list = field(default_factory=list)
    sections: list = field(default_factory=list)
    faculties: list = field(default_factory=list)
    rooms: list = field(default_factory=list)
    labs: list = field(default_factory=list)

    # Generated Data
    timeslots: list = field(default_factory=list)
    activities: list = field(default_factory=list)

    # Scheduler Output
    assignments: list = field(default_factory=list)
    scheduled_classes: list = field(default_factory=list)

    # Runtime Calendars
    faculty_schedule: dict = field(default_factory=dict)
    room_schedule: dict = field(default_factory=dict)
    section_schedule: dict = field(default_factory=dict)