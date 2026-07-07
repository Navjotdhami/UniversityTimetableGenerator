from dataclasses import dataclass, field


@dataclass
class SchedulerContext:

    courses: list = field(default_factory=list)

    sections: list = field(default_factory=list)

    faculties: list = field(default_factory=list)

    rooms: list = field(default_factory=list)

    labs: list = field(default_factory=list)

    timeslots: list = field(default_factory=list)

    scheduled_classes: list = field(default_factory=list)